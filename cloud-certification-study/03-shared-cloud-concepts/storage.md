# 💾 Storage (Concept + AWS↔Azure)

> **Concept note:** Three storage types. Pick by *how* you access the data.

## The 3 storage types
| Type | What it's for | Analogy |
|---|---|---|
| **Object** | Files/blobs accessed via API (images, data, backups, data lakes) | A giant key-value locker |
| **Block** | Disks attached to VMs (OS, databases) | A hard drive |
| **File** | Shared network drive (SMB/NFS) | A team shared folder |

## AWS ↔ Azure service mapping
| Capability | AWS | Azure |
|---|---|---|
| Object storage | S3 | Blob Storage |
| Block (VM disks) | EBS | Managed Disks |
| File shares | EFS / FSx | Azure Files |
| Archive/cold | S3 Glacier | Blob Archive tier |
| Hybrid/on-prem gateway | Storage Gateway | Azure File Sync / StorSimple |

## Storage tiers (cost vs access speed)
| Hot/frequent | Infrequent | Archive |
|---|---|---|
| S3 Standard / Blob Hot | S3 Standard-IA / Blob Cool | S3 Glacier / Blob Archive |

## Redundancy
- **AWS:** data replicated across AZs within a region by default (S3); cross-region replication optional.
- **Azure:** LRS (local), ZRS (zones), GRS/GZRS (geo). Memorize these for AZ-104/AZ-900.

## Hands-on lab
- Create a bucket/container, upload a file, set lifecycle to move to cool/archive.
- **Cleanup:** delete objects + bucket / delete resource group.

## ⚠️ Common exam traps
- Object storage ≠ a file system; no in-place edits, you replace objects.
- Choosing wrong redundancy (GRS for cost-sensitive, LRS for compliance needing geo).
- Retrieval from archive tiers has **delay + cost**.

## 🃏 Flashcards
| Q | A |
|---|---|
| AWS object storage? | S3 |
| Azure object storage? | Blob Storage |
| Geo-redundant in Azure? | GRS/GZRS |
| Cheapest archival (AWS)? | S3 Glacier Deep Archive |
| Shared network drive (Azure)? | Azure Files |

🔗 Related: [[data-engineering]] · [[cost-optimization]]
