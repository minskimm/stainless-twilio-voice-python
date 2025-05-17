# Changelog

## 0.1.0-alpha.1 (2025-05-17)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/minskimm/stainless-twilio-voice-python/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **api:** update via SDK Studio ([247b776](https://github.com/minskimm/stainless-twilio-voice-python/commit/247b77676ef5e7ac5a9312566aa0b93fb4efe4dc))
* **api:** update via SDK Studio ([b6858f5](https://github.com/minskimm/stainless-twilio-voice-python/commit/b6858f5b9ed0a6f1287b4c9b854a32215189c365))
* **api:** update via SDK Studio ([88f6eff](https://github.com/minskimm/stainless-twilio-voice-python/commit/88f6effc62eeb0f01f02c9e980262c3f70500ade))
* **api:** update via SDK Studio ([cf08769](https://github.com/minskimm/stainless-twilio-voice-python/commit/cf08769ec3c14fcc2b1a423b50fc4f0e9d5e87dc))
* **client:** add support for endpoint-specific base URLs ([750c8e1](https://github.com/minskimm/stainless-twilio-voice-python/commit/750c8e17f184a968328d4652926e7723d56cc2cc))


### Bug Fixes

* **ci:** ensure pip is always available ([85419cf](https://github.com/minskimm/stainless-twilio-voice-python/commit/85419cfd5fcfa43a40ae3e747bd207b3dd31a787))
* **ci:** remove publishing patch ([1ccd1ac](https://github.com/minskimm/stainless-twilio-voice-python/commit/1ccd1ac152342aba835320b30505494113440b20))
* **package:** support direct resource imports ([852af13](https://github.com/minskimm/stainless-twilio-voice-python/commit/852af13736aafbb59082d5129bae9be0d130d6cb))
* **perf:** optimize some hot paths ([b557adb](https://github.com/minskimm/stainless-twilio-voice-python/commit/b557adb0b69f80807b87dbd80ba140566e298b9d))
* **perf:** skip traversing types for NotGiven values ([52b1a29](https://github.com/minskimm/stainless-twilio-voice-python/commit/52b1a29ed216cea8c6db3471753246f66180d16a))
* **pydantic v1:** more robust ModelField.annotation check ([ec26303](https://github.com/minskimm/stainless-twilio-voice-python/commit/ec263038920aef41feb8f4d1a8c9fcd24bd7e475))
* **types:** handle more discriminated union shapes ([1e7434c](https://github.com/minskimm/stainless-twilio-voice-python/commit/1e7434c344403b55ec71e045a63cad981070a750))


### Chores

* broadly detect json family of content-type headers ([2f3a51e](https://github.com/minskimm/stainless-twilio-voice-python/commit/2f3a51e640827d412aa22f5af9a7335253b390b1))
* **ci:** add timeout thresholds for CI jobs ([64dcbd9](https://github.com/minskimm/stainless-twilio-voice-python/commit/64dcbd9c851d4c92f0e4f2dfa1446d2b25d8f8da))
* **ci:** fix installation instructions ([d69f84e](https://github.com/minskimm/stainless-twilio-voice-python/commit/d69f84ed8de886193d0717ca66e755916d1f0f55))
* **ci:** only use depot for staging repos ([1c72126](https://github.com/minskimm/stainless-twilio-voice-python/commit/1c72126004749318d5632114aca3f801cbbaea5c))
* **ci:** upload sdks to package manager ([c2e04ce](https://github.com/minskimm/stainless-twilio-voice-python/commit/c2e04ce7eba73a6bba4081f9463a2682a1733400))
* **client:** minor internal fixes ([d3e7faf](https://github.com/minskimm/stainless-twilio-voice-python/commit/d3e7fafe120f053f22e2cfa1462920e6f5a50b44))
* fix typos ([#3](https://github.com/minskimm/stainless-twilio-voice-python/issues/3)) ([1885813](https://github.com/minskimm/stainless-twilio-voice-python/commit/18858136b9ace6a7b3dc2c4a3b34bf888c05913b))
* go live ([#1](https://github.com/minskimm/stainless-twilio-voice-python/issues/1)) ([00ce234](https://github.com/minskimm/stainless-twilio-voice-python/commit/00ce2348962d0300941ea604faa0a55d2397714e))
* **internal:** avoid errors for isinstance checks on proxies ([1dba3b4](https://github.com/minskimm/stainless-twilio-voice-python/commit/1dba3b45740c93a0dea861c15c3bbcd0eca3775e))
* **internal:** base client updates ([a555465](https://github.com/minskimm/stainless-twilio-voice-python/commit/a555465d6ad4ace05217e6f11fbdeaddc4aac133))
* **internal:** bump pyright version ([139a2e4](https://github.com/minskimm/stainless-twilio-voice-python/commit/139a2e4030c22f1ff7fa4bdc741d9f3309f18e65))
* **internal:** bump rye to 0.44.0 ([273e663](https://github.com/minskimm/stainless-twilio-voice-python/commit/273e663abca17116796ac99f4d1bbc382419eecf))
* **internal:** codegen related update ([567abb4](https://github.com/minskimm/stainless-twilio-voice-python/commit/567abb4a4a5c6f31ca559c0532f95904d5e78ec4))
* **internal:** codegen related update ([dac4552](https://github.com/minskimm/stainless-twilio-voice-python/commit/dac4552b8fa12b5f1bfc9772394bb06ba8ed13c6))
* **internal:** codegen related update ([48d1484](https://github.com/minskimm/stainless-twilio-voice-python/commit/48d148417025748c2079e56da33675290a28746f))
* **internal:** codegen related update ([8c99534](https://github.com/minskimm/stainless-twilio-voice-python/commit/8c9953428653f15a25538d4d436020791ae1db34))
* **internal:** codegen related update ([34c2f31](https://github.com/minskimm/stainless-twilio-voice-python/commit/34c2f312a23fd30fae3a85e1d7a512d0c3b8ef81))
* **internal:** expand CI branch coverage ([fbe410b](https://github.com/minskimm/stainless-twilio-voice-python/commit/fbe410b0e29d831fc3ea1f7baf1e9e150048a4ce))
* **internal:** fix list file params ([a546f52](https://github.com/minskimm/stainless-twilio-voice-python/commit/a546f52cd203e02781abf615ee1ed3476bfc017a))
* **internal:** import reformatting ([25795ed](https://github.com/minskimm/stainless-twilio-voice-python/commit/25795edab27251a9e69e770cf7e896442df197c3))
* **internal:** reduce CI branch coverage ([ec8863b](https://github.com/minskimm/stainless-twilio-voice-python/commit/ec8863b6d63f3333248ab5b5d710baf9388d10b7))
* **internal:** refactor retries to not use recursion ([4841ad1](https://github.com/minskimm/stainless-twilio-voice-python/commit/4841ad1a4ce2c3a83c0a57ce6ce9f7aeceb54afe))
* **internal:** remove extra empty newlines ([6f07cb5](https://github.com/minskimm/stainless-twilio-voice-python/commit/6f07cb5c1c25800bd291a7887abefc97f32ada26))
* **internal:** remove trailing character ([#4](https://github.com/minskimm/stainless-twilio-voice-python/issues/4)) ([c290b4e](https://github.com/minskimm/stainless-twilio-voice-python/commit/c290b4e149d829689ee0e71ca20a64fe3ed3dc02))
* **internal:** slight transform perf improvement ([#5](https://github.com/minskimm/stainless-twilio-voice-python/issues/5)) ([90e3815](https://github.com/minskimm/stainless-twilio-voice-python/commit/90e3815c980be50b883f413fd7f905f0950e83f6))
* **internal:** update models test ([ee657b2](https://github.com/minskimm/stainless-twilio-voice-python/commit/ee657b230f7381c7e9cff5903565c6aac764cf15))
* **internal:** update pyright settings ([b03c2cb](https://github.com/minskimm/stainless-twilio-voice-python/commit/b03c2cb0a94c465187cf1edc3bc9ebe4842041e6))
* **tests:** improve enum examples ([#6](https://github.com/minskimm/stainless-twilio-voice-python/issues/6)) ([23551f3](https://github.com/minskimm/stainless-twilio-voice-python/commit/23551f3fa503ff79656ddcdb9c7a3fcb038716bc))


### Documentation

* remove or fix invalid readme examples ([f8e5437](https://github.com/minskimm/stainless-twilio-voice-python/commit/f8e543787f77fc2b7f72eec32025e9b419e802d2))
* remove private imports from datetime snippets ([0bf43a6](https://github.com/minskimm/stainless-twilio-voice-python/commit/0bf43a6f53c40b466cf3902acea9d14246abc509))
