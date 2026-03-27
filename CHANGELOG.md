# Changelog

## 0.13.0 (2026-03-27)

Full Changelog: [v0.12.0...v0.13.0](https://github.com/evrimai/fleet-client/compare/v0.12.0...v0.13.0)

### Features

* **api:** api update ([0cff1ab](https://github.com/evrimai/fleet-client/commit/0cff1abab94baccb747fe7c93b22a3345e0da2e5))
* **api:** api update ([f36d6b7](https://github.com/evrimai/fleet-client/commit/f36d6b79b5c43847654a49375ea67f85c26fd07d))
* **api:** api update ([a255932](https://github.com/evrimai/fleet-client/commit/a25593211cd94d196d67f74c3c99bdd5cfb698c8))
* **api:** api update ([930bbde](https://github.com/evrimai/fleet-client/commit/930bbdea7c63924ce121241d388aec24774e1c5d))
* **api:** manual updates ([e110e16](https://github.com/evrimai/fleet-client/commit/e110e1629b9f7c14f848d73f22443f2a112a6b2e))
* **client:** add custom JSON encoder for extended type support ([b12f4cf](https://github.com/evrimai/fleet-client/commit/b12f4cf8234dbe380527e80a9909e13889b3ee80))
* **client:** add support for binary request streaming ([2bbd1ac](https://github.com/evrimai/fleet-client/commit/2bbd1ac0fe78029d434727ef17f34cb984c128c8))
* **internal:** implement indices array format for query and form serialization ([53fbee9](https://github.com/evrimai/fleet-client/commit/53fbee972c5a480b85ec840e21e3c90c831da39a))


### Bug Fixes

* **deps:** bump minimum typing-extensions version ([9db556a](https://github.com/evrimai/fleet-client/commit/9db556a6bc9b5b9e2c76ed7c8d14e9f05c3aefa9))
* **pydantic:** do not pass `by_alias` unless set ([7e5a198](https://github.com/evrimai/fleet-client/commit/7e5a198d7414e086680fd03a5d5dfb71c216e206))
* sanitize endpoint path params ([a88f326](https://github.com/evrimai/fleet-client/commit/a88f326c5dec6d10c75320451d0277a8e65f3199))
* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([23f42b6](https://github.com/evrimai/fleet-client/commit/23f42b615ba4b6a3daaa218df417981c73e407ac))
* use async_to_httpx_files in patch method ([ffad06e](https://github.com/evrimai/fleet-client/commit/ffad06e55e66e787730495a50d67ebb96280e5c3))


### Chores

* add missing docstrings ([736494d](https://github.com/evrimai/fleet-client/commit/736494d0437e8b474aafd91e522aeadcbb735d55))
* **ci:** skip lint on metadata-only changes ([5989c91](https://github.com/evrimai/fleet-client/commit/5989c916bce654b7d858f91241190394fb6f78d5))
* **ci:** skip uploading artifacts on stainless-internal branches ([559cf1b](https://github.com/evrimai/fleet-client/commit/559cf1b2abf5ab41424f8b5f93b5fd881d3ffa0a))
* **ci:** upgrade `actions/github-script` ([0ca647c](https://github.com/evrimai/fleet-client/commit/0ca647c217605a9641c688c5edf00bd975c3e890))
* format all `api.md` files ([c9380af](https://github.com/evrimai/fleet-client/commit/c9380afc68acf3eaf0f36b0d7f28a4d9af470bd2))
* **internal:** add `--fix` argument to lint script ([d32039b](https://github.com/evrimai/fleet-client/commit/d32039bd846070e7afcf51d78b1da2e45b496136))
* **internal:** add missing files argument to base client ([d1ac3d2](https://github.com/evrimai/fleet-client/commit/d1ac3d2bef5bbd4a9f330a46766cfd62d78d3541))
* **internal:** add request options to SSE classes ([65e4b03](https://github.com/evrimai/fleet-client/commit/65e4b0314eaf94efc5ac568100fc030850dad76a))
* **internal:** bump dependencies ([40b0e82](https://github.com/evrimai/fleet-client/commit/40b0e822038cf559af7a209b84cdbc0975df4241))
* **internal:** codegen related update ([77f60cb](https://github.com/evrimai/fleet-client/commit/77f60cb97fd34fd42528c08a340d1f766420ab28))
* **internal:** fix lint error on Python 3.14 ([92818ec](https://github.com/evrimai/fleet-client/commit/92818ec3d38ea49a62f9aa37a260273af0758209))
* **internal:** make `test_proxy_environment_variables` more resilient ([3a01ba6](https://github.com/evrimai/fleet-client/commit/3a01ba677e2005d49c3e8eff656ca5ae87f75349))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([8a62159](https://github.com/evrimai/fleet-client/commit/8a62159e0a0cd23c1682b1979dd03ce426bc67ec))
* **internal:** remove mock server code ([e15bf75](https://github.com/evrimai/fleet-client/commit/e15bf75b79e801b349340b3a48d1bbf4a912506f))
* **internal:** tweak CI branches ([3abff28](https://github.com/evrimai/fleet-client/commit/3abff2882a75ed0bce211e13336e9d002d5cbf41))
* **internal:** update `actions/checkout` version ([fbbe10e](https://github.com/evrimai/fleet-client/commit/fbbe10ef1dbd881f2cde06f2f6d94010e474883b))
* **internal:** update gitignore ([fb28fa8](https://github.com/evrimai/fleet-client/commit/fb28fa8c75e687e848515b6eee27a0215db7ad10))
* speedup initial import ([620c4e4](https://github.com/evrimai/fleet-client/commit/620c4e40630bdb35d5383b1a50b4fbf781127776))
* update mock server docs ([19e2ac9](https://github.com/evrimai/fleet-client/commit/19e2ac9c3411e4c2d1f62534f0eb287f6ba3ef49))

## 0.12.0 (2025-12-03)

Full Changelog: [v0.11.0...v0.12.0](https://github.com/evrimai/fleet-client/compare/v0.11.0...v0.12.0)

### Features

* **api:** api update ([a4c8a84](https://github.com/evrimai/fleet-client/commit/a4c8a846fc578f5fabb97debe19a4b55d35816d8))


### Bug Fixes

* compat with Python 3.14 ([7208cd4](https://github.com/evrimai/fleet-client/commit/7208cd4656f976d64989c83debce60994342ec3d))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([ba78018](https://github.com/evrimai/fleet-client/commit/ba78018d50077bf7286fdf7e3b21bb1d66eb53c1))
* ensure streams are always closed ([5071426](https://github.com/evrimai/fleet-client/commit/5071426b949c763783ffe6a0748c3118790e1d48))


### Chores

* add Python 3.14 classifier and testing ([f776bfd](https://github.com/evrimai/fleet-client/commit/f776bfdbe0973a7cde4ce5fb6504d3082ccc35ab))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([b311753](https://github.com/evrimai/fleet-client/commit/b311753843e851a06002909fbcb115b57842c12a))
* **docs:** use environment variables for authentication in code snippets ([f462dbc](https://github.com/evrimai/fleet-client/commit/f462dbc8e6fa8ed3654e018a1ed03c14d89fba65))
* **internal:** grammar fix (it's -&gt; its) ([2e6bb7d](https://github.com/evrimai/fleet-client/commit/2e6bb7dd451b99c701959826a8b94766cc89eaad))
* **package:** drop Python 3.8 support ([8168e44](https://github.com/evrimai/fleet-client/commit/8168e445238b33a92f7af5dfdfeed08a3f416c7e))
* update lockfile ([3024bbc](https://github.com/evrimai/fleet-client/commit/3024bbc7d93f3154d44b6ba52838edc7320dfbc9))

## 0.11.0 (2025-11-02)

Full Changelog: [v0.10.0...v0.11.0](https://github.com/evrimai/fleet-client/compare/v0.10.0...v0.11.0)

### Features

* **api:** api update ([f0637a3](https://github.com/evrimai/fleet-client/commit/f0637a365e093974767a1df3e0ade58316cd22fd))

## 0.10.0 (2025-11-02)

Full Changelog: [v0.9.0...v0.10.0](https://github.com/evrimai/fleet-client/compare/v0.9.0...v0.10.0)

### Features

* **api:** api update ([284b65f](https://github.com/evrimai/fleet-client/commit/284b65f9b3d621a46550b4f1903b76425e4d70e3))
* **api:** api update ([fbe9698](https://github.com/evrimai/fleet-client/commit/fbe96981657c96c3b0c2d17b5ac2c8dd3356866c))
* **api:** manual updates ([97ddb81](https://github.com/evrimai/fleet-client/commit/97ddb8184e4575548fce8484c2b30143e6c3b85b))


### Chores

* **internal/tests:** avoid race condition with implicit client cleanup ([1e9b188](https://github.com/evrimai/fleet-client/commit/1e9b1887c9e824ea2eed742fef0137a049862a74))

## 0.9.0 (2025-10-31)

Full Changelog: [v0.8.0...v0.9.0](https://github.com/evrimai/fleet-client/compare/v0.8.0...v0.9.0)

### Features

* **api:** api update ([51584d2](https://github.com/evrimai/fleet-client/commit/51584d2fd754afcddcf6655ff67bc761fea45a51))
* **api:** manual updates ([375ffb9](https://github.com/evrimai/fleet-client/commit/375ffb99c18461572a4aebf1eb26028cb786672f))


### Bug Fixes

* **client:** close streams without requiring full consumption ([ddfceb0](https://github.com/evrimai/fleet-client/commit/ddfceb02c2d1bd42a7444c59ed42f8b28c9c70c7))

## 0.8.0 (2025-10-23)

Full Changelog: [v0.7.0...v0.8.0](https://github.com/evrimai/fleet-client/compare/v0.7.0...v0.8.0)

### Features

* **api:** api update ([4444dca](https://github.com/evrimai/fleet-client/commit/4444dca72fe6d5b36f225a6b2ad8c4d93c61a26c))
* **api:** api update ([f1e71cf](https://github.com/evrimai/fleet-client/commit/f1e71cf3ced33fbd321e3a5b37b405df99e762bd))

## 0.7.0 (2025-10-22)

Full Changelog: [v0.6.0...v0.7.0](https://github.com/evrimai/fleet-client/compare/v0.6.0...v0.7.0)

### Features

* **api:** api update ([be01898](https://github.com/evrimai/fleet-client/commit/be01898710be8527d4bafbd3913a89d0c75814d9))

## 0.6.0 (2025-10-21)

Full Changelog: [v0.5.0...v0.6.0](https://github.com/evrimai/fleet-client/compare/v0.5.0...v0.6.0)

### Features

* **api:** api update ([12e90ed](https://github.com/evrimai/fleet-client/commit/12e90edb57ac90c955b17ae65d024d93553283eb))
* **api:** api update ([79508da](https://github.com/evrimai/fleet-client/commit/79508da7d93a2b38aeb0dcef31cf721dc2be7c15))
* **api:** api update ([af8cacc](https://github.com/evrimai/fleet-client/commit/af8cacc836e4246dbf46229052dd166e2a79e386))
* **api:** manual updates ([44ee318](https://github.com/evrimai/fleet-client/commit/44ee3182469fbcda1ff23de5a707c09e9c921a8c))

## 0.5.0 (2025-10-21)

Full Changelog: [v0.4.0...v0.5.0](https://github.com/evrimai/fleet-client/compare/v0.4.0...v0.5.0)

### Features

* **api:** api update ([d412590](https://github.com/evrimai/fleet-client/commit/d41259033e4019c8b0bbae82a3777f61168ac613))
* **api:** manual updates ([64be9c1](https://github.com/evrimai/fleet-client/commit/64be9c1ce4656d6b8642a0c7c2ebfd7e18c00084))

## 0.4.0 (2025-10-21)

Full Changelog: [v0.3.0...v0.4.0](https://github.com/evrimai/fleet-client/compare/v0.3.0...v0.4.0)

### Features

* **api:** manual updates for owners ([eeb3e46](https://github.com/evrimai/fleet-client/commit/eeb3e46ceb951a44241af103613b8af6dd7f4fb8))

## 0.3.0 (2025-10-21)

Full Changelog: [v0.2.2...v0.3.0](https://github.com/evrimai/fleet-client/compare/v0.2.2...v0.3.0)

### Features

* **api:** api update ([38a7416](https://github.com/evrimai/fleet-client/commit/38a7416cf6ddd58aa1e7adb90b1d4eb704ff463f))
* **api:** api update ([dce1369](https://github.com/evrimai/fleet-client/commit/dce13692486dfd073ad58ade34d2888a6590660b))

## 0.2.2 (2025-10-18)

Full Changelog: [v0.2.1...v0.2.2](https://github.com/evrimai/fleet-client/compare/v0.2.1...v0.2.2)

### Chores

* sync repo ([29846d9](https://github.com/evrimai/fleet-client/commit/29846d9a1daeafb06856842be735ce3d2431445d))
* update SDK settings ([c115c3e](https://github.com/evrimai/fleet-client/commit/c115c3e4a83059d7df3cf24a79e410a7bbd20b36))
* update SDK settings ([1d925fe](https://github.com/evrimai/fleet-client/commit/1d925fe2b09a44b1264df8fc468a45abdf486d11))

## 0.2.1 (2025-10-18)

Full Changelog: [v0.2.0...v0.2.1](https://github.com/evrimai/fleet-client/compare/v0.2.0...v0.2.1)

### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([0f95f44](https://github.com/evrimai/fleet-client/commit/0f95f449a11fe83f6eafd99b93436d7ee58de168))

## 0.2.0 (2025-10-11)

Full Changelog: [v0.1.1...v0.2.0](https://github.com/evrimai/fleet-client/compare/v0.1.1...v0.2.0)

### Features

* improve future compat with pydantic v3 ([c8691f1](https://github.com/evrimai/fleet-client/commit/c8691f125561c469a298672d1e367111f7198bb3))
* **types:** replace List[str] with SequenceNotStr in params ([8f32157](https://github.com/evrimai/fleet-client/commit/8f3215724d47844374b296b5ba086c7947157cd0))


### Bug Fixes

* avoid newer type syntax ([2a164e8](https://github.com/evrimai/fleet-client/commit/2a164e875d4cd861b984e3615a78aac98b9265bd))


### Chores

* do not install brew dependencies in ./scripts/bootstrap by default ([f36a4cd](https://github.com/evrimai/fleet-client/commit/f36a4cd011f4a2918a8df46043ce06c0b09c2be5))
* **internal:** add Sequence related utils ([cd3e713](https://github.com/evrimai/fleet-client/commit/cd3e713c5830f3a836eedb2b975e22003d3f769c))
* **internal:** change ci workflow machines ([0df0fba](https://github.com/evrimai/fleet-client/commit/0df0fba25bab2a88dfdd10712882a3daf09a7be6))
* **internal:** detect missing future annotations with ruff ([929726d](https://github.com/evrimai/fleet-client/commit/929726daea0669365219252fe951eb45070274a1))
* **internal:** move mypy configurations to `pyproject.toml` file ([8d878bf](https://github.com/evrimai/fleet-client/commit/8d878bf66b804f2363d81cf11b8776cea71c3013))
* **internal:** update pydantic dependency ([15e929f](https://github.com/evrimai/fleet-client/commit/15e929fb7cb27e7d15c4482b12267d18092eebe6))
* **internal:** update pyright exclude list ([e3e3610](https://github.com/evrimai/fleet-client/commit/e3e36109bc89d95d2feca7f8d57c4b44a4b64cfa))
* **tests:** simplify `get_platform` test ([304818a](https://github.com/evrimai/fleet-client/commit/304818a66dc6b87b9d0dbf8962b1b0f74910f0ce))
* **types:** change optional parameter type from NotGiven to Omit ([e8fda68](https://github.com/evrimai/fleet-client/commit/e8fda68010aabfe3439560b04fae38537e7668fd))

## 0.1.1 (2025-08-22)

Full Changelog: [v0.1.0...v0.1.1](https://github.com/evrimai/fleet-client/compare/v0.1.0...v0.1.1)

### Chores

* update github action ([c381e7b](https://github.com/evrimai/fleet-client/commit/c381e7bf6e43d386fba8b6a0b97c640fc546252d))

## 0.1.0 (2025-08-12)

Full Changelog: [v0.0.1...v0.1.0](https://github.com/evrimai/fleet-client/compare/v0.0.1...v0.1.0)

### Chores

* update SDK settings ([cdf80fa](https://github.com/evrimai/fleet-client/commit/cdf80fa800399b84a4be3220a6700d29f6e63acf))
* update SDK settings ([7eb1ac3](https://github.com/evrimai/fleet-client/commit/7eb1ac32ce6ee54bffea2c5fdb51d7fdd3d760f1))
