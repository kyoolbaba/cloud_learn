---
tags: [mlops, hands-on, cloud-only, sagemaker, lab/capstone]
aliases: [MLOps Capstone, Auto-Retraining Loop]
cert: MLA-C01
---
> [[mlops/labs/L7-pipeline-cicd/README|◀ L7]] · [[mlops/README|MLOps track]] · [[portfolio/12-sagemaker-mlops/README|🗂️ Portfolio 12]] · [[MLA-C01|🎯 all domains]]

# 🏁 Capstone · The self-healing model loop

## 🎯 Goal
Wire L1–L7 into **one automated loop** that needs no human after setup:

```
new data → Pipeline (L7) trains + evaluates
         → if good → Model Registry (L3) [approval gate]
         → deploy endpoint (L5) with data capture (L6)
         → Model Monitor (L6) watches for drift
         → drift detected → EventBridge rule → re-run the Pipeline
         → ...loop forever, hands-off
```

This is the **portfolio piece** that proves you can run ML in production — the exact story
[[MLA-C01]] is built around.

## 💡 Why it matters
Anyone can train a model. **Almost no junior can show an automated retraining loop.** This is
your interview answer to *"have you done MLOps?"* — and it lives entirely in the cloud.

## 🧱 What you build (assembling the bricks)
| Brick | From lab | Role in the loop |
|---|---|---|
| Feature group | [[mlops/labs/L2-feature-store/README\|L2]] | consistent features for train + serve |
| Training/eval/register pipeline | [[mlops/labs/L7-pipeline-cicd/README\|L7]] | the retrain engine |
| Approval gate | [[mlops/labs/L3-train-and-register/README\|L3]] | only good models ship |
| Endpoint + data capture | [[mlops/labs/L5-realtime-endpoint/README\|L5]] + [[mlops/labs/L6-model-monitor/README\|L6]] | serve + record live traffic |
| Drift monitor | [[mlops/labs/L6-model-monitor/README\|L6]] | the trigger |
| **EventBridge rule** | *new here* | drift alarm → start pipeline |

## ☁️ The new glue: drift → retrain (EventBridge)
The one piece L1–L7 didn't cover — connect Model Monitor's CloudWatch alarm to a pipeline start.

```python
# Studio notebook — create the rule that restarts training when drift fires
import boto3, json
events = boto3.client("events"); sm = boto3.client("sagemaker")

# 1) rule: match Model Monitor "constraint violated" / CloudWatch alarm state change
events.put_rule(
    Name="mlops-drift-retrain",
    EventPattern=json.dumps({
        "source": ["aws.cloudwatch"],
        "detail-type": ["CloudWatch Alarm State Change"],
        "detail": {"alarmName": ["l6-drift-alarm"], "state": {"value": ["ALARM"]}},
    }),
)
# 2) target: a Lambda (or SageMaker Pipeline via API) that calls pipeline.start()
#    minimal version: target a Lambda that runs sm.start_pipeline_execution(
#        PipelineName="l7-train-register-pipeline")
print("drift→retrain rule created — the loop is now closed")
```

> The cleanest production wiring is **Model Monitor → CloudWatch alarm → EventBridge → Lambda →
> `start_pipeline_execution`**. Build the Lambda the same way you did in
> [[projects/10-cloudwatch-autostop/README|project 10]] (scheduled/event Lambda) — reuse that skill.

## ✅ Done when (capstone definition of done)
- [ ] A feature group feeds the pipeline (L2).
- [ ] The pipeline trains → evaluates → registers behind an approval gate (L7+L3).
- [ ] An endpoint serves predictions with data capture on (L5+L6).
- [ ] A monitoring schedule + CloudWatch alarm detect drift (L6).
- [ ] An EventBridge rule restarts the pipeline when the alarm fires.
- [ ] You can **draw the whole loop on a whiteboard** and name the AWS service at each arrow.

## 🧹 Teardown (do a full sweep — this lab leaves the most running)
```python
# delete in this order
mon.delete_monitoring_schedule()
predictor.delete_endpoint()
events.delete_rule(Name="mlops-drift-retrain", Force=True)
# fg.delete()  # feature group, if you're fully done
```
Confirm empty: **Endpoints**, **Monitoring schedules**, **EventBridge rules**. Then shut down the kernel.

## 🗂️ Make it a portfolio piece
Write it up in [[portfolio/12-sagemaker-mlops/README]]: the architecture diagram, the loop story,
a screenshot of the pipeline DAG + a drift report, and "what I'd do next" (canary deploys,
A/B, shadow testing). That note is your proof of work for ML Engineer roles.

## 📚 awesome-mlops links
*MLOps Core* + *Existing ML Systems* (see how Uber/Netflix/DoorDash run this exact loop at scale).

## 🔁 Azure ML equivalent
The whole loop ≈ Azure ML pipelines + model monitoring + **Event Grid** triggers + Azure Functions.

---
🎓 Finished the track? Update [[PROGRESS]] and [[portfolio/12-sagemaker-mlops/README]]. Back: [[mlops/README]]
