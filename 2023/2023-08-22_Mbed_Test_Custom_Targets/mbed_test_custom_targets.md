# Mbed 测试基于自定义板子

- compile
  -  `mbed test --source . --source mbed-targets --target LBSNB_FM33LE026_V0_2 -n TESTS-TEST_NBPROTOCAL-CODEC_TEST --compile`
- write to board
  - use jlink to write to board and restart board
- run test
  - `mbedhtrun --skip-flashing --skip-reset -p COM6:9600`