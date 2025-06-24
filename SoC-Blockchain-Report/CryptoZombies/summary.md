# 🧟 CryptoZombies

Covered:
- Learn Solidity through gamified lessons
- Creating and managing zombie structs
- Inheritance and ERC721 concepts

### 🧪 Zombie Factory:
```solidity
pragma solidity ^0.8.0;

contract ZombieFactory {
    struct Zombie {
        string name;
        uint dna;
    }

    Zombie[] public zombies;
}
```
