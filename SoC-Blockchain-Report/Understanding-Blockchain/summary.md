# ⛓️ Understanding Blockchain

Covered:
- What is a block?
- Hashing and SHA-256
- Blockchain structure
- Consensus mechanisms

### 🧪 Example Code:
```python
import hashlib

def hash_block(data):
    return hashlib.sha256(data.encode()).hexdigest()

print(hash_block("block data"))
```
