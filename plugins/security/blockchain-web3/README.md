# security-blockchain-web3

Smart-contract security, DeFi, Solidity and Web3 development.

## Install

```bash
/plugin marketplace add marslanalvi/SkillsStack
/plugin install security-blockchain-web3@skills-stack
```

## Skills (19)

| Skill | What it does | Created by | License |
|---|---|---|---|
| [algorand-vulnerability-scanner](skills/algorand-vulnerability-scanner/SKILL.md) | Scans Algorand smart contracts for 11 common vulnerabilities including rekeying attacks, unchecked transaction fees, missing field validations, and access control issues. Use when auditing Algorand p… | Trail of Bits | CC-BY-SA-4.0 |
| [blockrun](skills/blockrun/SKILL.md) | BlockRun works with Claude Code and Google Antigravity. | sickn33 and the agentic-awesome-skills contributors (copyri… | MIT (code) / CC-BY-4.0 (written content) |
| [cairo-vulnerability-scanner](skills/cairo-vulnerability-scanner/SKILL.md) | Scans Cairo/StarkNet smart contracts for 6 critical vulnerabilities including felt252 arithmetic overflow, L1-L2 messaging issues, address conversion problems, and signature replay. Use when auditing… | Trail of Bits | CC-BY-SA-4.0 |
| [cosmos-vulnerability-scanner](skills/cosmos-vulnerability-scanner/SKILL.md) | Scans Cosmos SDK blockchain modules and CosmWasm contracts for consensus-critical vulnerabilities — chain halts, fund loss, state divergence. 25 core + 16 IBC + 10 EVM + 3 CosmWasm patterns. Use when… | Trail of Bits | CC-BY-SA-4.0 |
| [defi-amm-security](skills/defi-amm-security/SKILL.md) | Security checklist for Solidity AMM contracts, liquidity pools, and swap flows. Covers reentrancy, CEI ordering, donation or inflation attacks, oracle manipulation, slippage, admin controls, and inte… | Affaan Mustafa | MIT |
| [defi-protocol-templates](skills/defi-protocol-templates/SKILL.md) | Implement DeFi protocols with production-ready templates for staking, AMMs, governance, and flash loans. Use when building decentralized finance applications or smart contract protocols. | Seth Hobson | MIT |
| [entry-point-analyzer](skills/entry-point-analyzer/SKILL.md) | Analyzes smart contract codebases to identify state-changing entry points for security auditing. Detects externally callable functions that modify state, categorizes them by access level (public, adm… | Trail of Bits | CC-BY-SA-4.0 |
| [evm-token-decimals](skills/evm-token-decimals/SKILL.md) | Prevent silent decimal mismatch bugs across EVM chains. Covers runtime decimal lookup, chain-aware caching, bridged-token precision drift, and safe normalization for bots, dashboards, and DeFi tools.… | Affaan Mustafa | MIT |
| [guidelines-advisor](skills/guidelines-advisor/SKILL.md) | Smart contract development advisor based on Trail of Bits' best practices. Analyzes codebase to generate documentation/specifications, review architecture, check upgradeability patterns, assess imple… | Trail of Bits | CC-BY-SA-4.0 |
| [llm-trading-agent-security](skills/llm-trading-agent-security/SKILL.md) | Security patterns for autonomous trading agents with wallet or transaction authority. Covers prompt injection, spend limits, pre-send simulation, circuit breakers, MEV protection, and key handling. U… | Affaan Mustafa | MIT |
| [moltnode-chain-reader](skills/moltnode-chain-reader/SKILL.md) | Read 31 blockchains over keyless JSON-RPC with MoltNode (balances, blocks, contract calls) and get Chord swap quotes with an unsigned transaction and simulation. | Chord | MIT |
| [nft-standards](skills/nft-standards/SKILL.md) | Implement NFT standards (ERC-721, ERC-1155) with proper metadata handling, minting strategies, and marketplace integration. Use when creating NFT contracts, building NFT marketplaces, or implementing… | Seth Hobson | MIT |
| [secure-workflow-guide](skills/secure-workflow-guide/SKILL.md) | Guides through Trail of Bits' 5-step secure development workflow. Runs Slither scans, checks special features (upgradeability/ERC conformance/token integration), generates visual security diagrams, h… | Trail of Bits | CC-BY-SA-4.0 |
| [solana-vulnerability-scanner](skills/solana-vulnerability-scanner/SKILL.md) | Scans Solana programs for 6 critical vulnerabilities including arbitrary CPI, improper PDA validation, missing signer/ownership checks, and sysvar spoofing. Use when auditing Solana/Anchor programs. | Trail of Bits | CC-BY-SA-4.0 |
| [solidity-security](skills/solidity-security/SKILL.md) | Master smart contract security best practices to prevent common vulnerabilities and implement secure Solidity patterns. Use when writing smart contracts, auditing existing contracts, or implementing… | Seth Hobson | MIT |
| [substrate-vulnerability-scanner](skills/substrate-vulnerability-scanner/SKILL.md) | Scans Substrate/Polkadot pallets for 7 critical vulnerabilities including arithmetic overflow, panic DoS, incorrect weights, and bad origin checks. Use when auditing Substrate runtimes or FRAME palle… | Trail of Bits | CC-BY-SA-4.0 |
| [token-integration-analyzer](skills/token-integration-analyzer/SKILL.md) | Token integration and implementation analyzer based on Trail of Bits' token integration checklist. Analyzes token implementations for ERC20/ERC721 conformity, checks for 20+ weird token patterns, ass… | Trail of Bits | CC-BY-SA-4.0 |
| [ton-vulnerability-scanner](skills/ton-vulnerability-scanner/SKILL.md) | Scans TON (The Open Network) smart contracts for 3 critical vulnerabilities including integer-as-boolean misuse, fake Jetton contracts, and forward TON without gas checks. Use when auditing FunC cont… | Trail of Bits | CC-BY-SA-4.0 |
| [web3-testing](skills/web3-testing/SKILL.md) | Test smart contracts comprehensively using Hardhat and Foundry with unit tests, integration tests, and mainnet forking. Use when testing Solidity contracts, setting up blockchain test suites, or vali… | Seth Hobson | MIT |

## Credit and licenses

Every skill in this plugin was created by the people named above and collected into Skills Stack, which compiles open-source skills in one place. The authors keep all rights to their work. Each skill folder has an `ATTRIBUTION.md` with its full credit, license and any changes Skills Stack made, and the full license texts are in [LICENSES/](LICENSES).
