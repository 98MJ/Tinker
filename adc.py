import smbus2
import time

# I2C 버스 번호와 ADC 주소 설정
bus_number = 1
adc_address = 0x48

# I2C 버스 초기화
bus = smbus2.SMBus(bus_number)

# ADC 채널 설정 (0부터 3까지의 채널 사용 가능)
adc_channel = 0

# ADC 값 읽어오는 함수
def read_adc_value():
    # I2C 통신을 통해 ADC 값 읽기
    adc_value = bus.read_i2c_block_data(adc_address, adc_channel, 2)
    
    # ADC 값 계산
    value = (adc_value[0] << 8) | adc_value[1]
    
    return value

# 메인 루프
while True:
    try:
        # ADC 값 읽어오기
        adc_value = read_adc_value()
        
        # 읽어온 ADC 값 출력
        print("ADC 값: {}".format(adc_value))
        
        # 적절한 딜레이
        time.sleep(0.5)
    
    # Ctrl+C를 눌러 프로그램 종료
    except KeyboardInterrupt:
        break

# I2C 버스 닫기
bus.close()
