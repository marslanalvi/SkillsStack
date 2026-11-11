# security-fuzzing

Fuzzing, sanitizers, property-based and cryptographic testing.

## Install

```bash
/plugin marketplace add marslanalvi/SkillsStack
/plugin install security-fuzzing@skills-stack
```

## Skills (19)

| Skill | What it does | Created by | License |
|---|---|---|---|
| [address-sanitizer](skills/address-sanitizer/SKILL.md) | Builds and runs code under AddressSanitizer to catch buffer overflows, use-after-free, and other memory errors during fuzzing or tests. Covers -fsanitize=address builds, ASAN_OPTIONS, reading the cra… | Trail of Bits | CC-BY-SA-4.0 |
| [aflpp](skills/aflpp/SKILL.md) | Sets up and runs AFL++ for multi-core fuzzing of C/C++ projects built with afl-clang-fast or afl-gcc-fast. Covers instrumentation modes, parallel main and secondary campaigns, persistent mode, corpus… | Trail of Bits | CC-BY-SA-4.0 |
| [atheris](skills/atheris/SKILL.md) | Sets up and runs Atheris, the coverage-guided Python fuzzer built on libFuzzer. Covers TestOneInput harnesses, FuzzedDataProvider, instrumenting both pure Python and native C extensions, and running… | Trail of Bits | CC-BY-SA-4.0 |
| [cargo-fuzz](skills/cargo-fuzz/SKILL.md) | Sets up and runs cargo-fuzz, the standard fuzzing tool for Cargo-based Rust projects. Covers cargo fuzz init, the nightly toolchain requirement, fuzz_target! harnesses, Arbitrary-derived structured i… | Trail of Bits | CC-BY-SA-4.0 |
| [constant-time-analysis](skills/constant-time-analysis/SKILL.md) | Detects timing side-channel vulnerabilities in cryptographic code. Use when implementing or reviewing crypto code, encountering division on secrets, secret-dependent branches, or constant-time progra… | Trail of Bits | CC-BY-SA-4.0 |
| [constant-time-testing](skills/constant-time-testing/SKILL.md) | Measures timing side channels in cryptographic implementations by running them, using dudect for statistical analysis and Timecop over Valgrind for dynamic tracing. Covers the formal, symbolic, dynam… | Trail of Bits | CC-BY-SA-4.0 |
| [coverage-analysis](skills/coverage-analysis/SKILL.md) | Measures and interprets what a fuzzing campaign actually reaches, using llvm-cov, lcov, or a fuzzer's own coverage output. Covers baselining a new campaign, reading coverage reports, and turning unco… | Trail of Bits | CC-BY-SA-4.0 |
| [fuzzing-dictionary](skills/fuzzing-dictionary/SKILL.md) | Builds and applies fuzzing dictionaries so a fuzzer can produce the keywords, magic bytes, and tokens a target expects. Covers extracting tokens from source, headers, binaries, and specifications, di… | Trail of Bits | CC-BY-SA-4.0 |
| [fuzzing-obstacles](skills/fuzzing-obstacles/SKILL.md) | Patches past the barriers that stop a fuzzer making progress — checksum and hash verification, magic-value validation, time-based seeds, and other non-deterministic global state. Covers locating the… | Trail of Bits | CC-BY-SA-4.0 |
| [genotoxic](skills/genotoxic/SKILL.md) | Graph-informed mutation testing triage. Parses codebases with Trailmark, runs mutation testing and necessist, then uses survived mutants, unnecessary test statements, and call graph data to identify… | Trail of Bits | CC-BY-SA-4.0 |
| [harness-writing](skills/harness-writing/SKILL.md) | Designs and improves fuzzing harnesses for C/C++ and Rust. Covers mapping raw bytes onto a target API, generating structured inputs, avoiding non-determinism and false crashes, and deciding what to f… | Trail of Bits | CC-BY-SA-4.0 |
| [libafl](skills/libafl/SKILL.md) | Builds custom fuzzers with LibAFL, the modular Rust fuzzing library. Covers composing observers, feedbacks, mutators, schedulers, and executors into a fuzzer for targets the standard tools do not fit… | Trail of Bits | CC-BY-SA-4.0 |
| [libfuzzer](skills/libfuzzer/SKILL.md) | Sets up and runs libFuzzer, the coverage-guided fuzzer built into LLVM, on C/C++ code that compiles with Clang. Covers harness structure, -fsanitize=fuzzer builds, corpus and dictionary management, s… | Trail of Bits | CC-BY-SA-4.0 |
| [ossfuzz](skills/ossfuzz/SKILL.md) | Enrolls a project in OSS-Fuzz, Google's free continuous fuzzing service for open source, and drives it locally. Covers project.yaml, Dockerfile and build.sh setup, the helper scripts, reproducing OSS… | Trail of Bits | CC-BY-SA-4.0 |
| [property-based-testing](skills/property-based-testing/SKILL.md) | Writes, reviews, and debugs property-based tests — Hypothesis, fast-check, proptest, jqwik, rapid, and Echidna or Medusa for Solidity invariants. Use whenever tests should cover a whole input domain… | Trail of Bits | CC-BY-SA-4.0 |
| [ruzzy](skills/ruzzy/SKILL.md) | Sets up and runs Ruzzy, Trail of Bits' coverage-guided Ruby fuzzer and the only production-ready one for the language. Covers harness structure, fuzzing pure Ruby and the native C extensions in gems,… | Trail of Bits | CC-BY-SA-4.0 |
| [testing-handbook-generator](skills/testing-handbook-generator/SKILL.md) | Generates Claude Code skills from the Trail of Bits Testing Handbook (appsec.guide), analyzing handbook pages and emitting SKILL.md files with the structure each skill type requires. Use when creatin… | Trail of Bits | CC-BY-SA-4.0 |
| [vector-forge](skills/vector-forge/SKILL.md) | Mutation-driven test vector generation. Finds implementations of a cryptographic algorithm or protocol, runs mutation testing to identify escaped mutants, then generates new test vectors that deliber… | Trail of Bits | CC-BY-SA-4.0 |
| [wycheproof](skills/wycheproof/SKILL.md) | Validates cryptographic implementations against Project Wycheproof's test vectors, which encode known attacks and edge cases across AES, RSA, ECDSA, ECDH, and more. Covers loading test vectors, mappi… | Trail of Bits | CC-BY-SA-4.0 |

## Credit and licenses

Every skill in this plugin was created by the people named above and collected into Skills Stack, which compiles open-source skills in one place. The authors keep all rights to their work. Each skill folder has an `ATTRIBUTION.md` with its full credit, license and any changes Skills Stack made, and the full license texts are in [LICENSES/](LICENSES).
