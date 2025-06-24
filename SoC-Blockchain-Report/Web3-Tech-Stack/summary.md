# 🌐 Web3 Tech Stack

Covered:
- Web3.js vs Ethers.js
- Connecting with Metamask
- Interacting with Smart Contracts from frontend

### 🧪 Example DApp Code:
```javascript
const ethers = require("ethers");
async function connect() {
    if (window.ethereum) {
        await window.ethereum.request({ method: "eth_requestAccounts" });
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        console.log("Connected!", provider);
    }
}
```
