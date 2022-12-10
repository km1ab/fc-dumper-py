EESchema Schematic File Version 4
LIBS:test-cache
EELAYER 29 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date "15 nov 2012"
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L power:+5V #PWR06
U 1 1 580C1B61
P 3100 950
F 0 "#PWR06" H 3100 800 50  0001 C CNN
F 1 "+5V" H 3100 1090 50  0000 C CNN
F 2 "" H 3100 950 50  0000 C CNN
F 3 "" H 3100 950 50  0000 C CNN
	1    3100 950 
	1    0    0    -1  
$EndComp
Wire Wire Line
	3100 950  3100 1100
Wire Wire Line
	3100 1100 2900 1100
Wire Wire Line
	3100 1200 2900 1200
Connection ~ 3100 1100
$Comp
L power:GND #PWR05
U 1 1 580C1D11
P 3000 3150
F 0 "#PWR05" H 3000 2900 50  0001 C CNN
F 1 "GND" H 3000 3000 50  0000 C CNN
F 2 "" H 3000 3150 50  0000 C CNN
F 3 "" H 3000 3150 50  0000 C CNN
	1    3000 3150
	1    0    0    -1  
$EndComp
Wire Wire Line
	3000 1300 3000 1700
Wire Wire Line
	3000 2700 2900 2700
Wire Wire Line
	3000 2500 2900 2500
Connection ~ 3000 2700
Wire Wire Line
	3000 2000 2900 2000
Connection ~ 3000 2500
Wire Wire Line
	3000 1700 2900 1700
Connection ~ 3000 2000
$Comp
L power:GND #PWR02
U 1 1 580C1E01
P 2300 3150
F 0 "#PWR02" H 2300 2900 50  0001 C CNN
F 1 "GND" H 2300 3000 50  0000 C CNN
F 2 "" H 2300 3150 50  0000 C CNN
F 3 "" H 2300 3150 50  0000 C CNN
	1    2300 3150
	1    0    0    -1  
$EndComp
Wire Wire Line
	2300 3000 2400 3000
Wire Wire Line
	2300 1500 2300 2300
Wire Wire Line
	2300 2300 2400 2300
Connection ~ 2300 3000
Connection ~ 2200 1100
Wire Wire Line
	2200 1900 2400 1900
Wire Wire Line
	2200 1100 2400 1100
Wire Wire Line
	2200 950  2200 1100
$Comp
L power:+3.3V #PWR01
U 1 1 580C1BC1
P 2200 950
F 0 "#PWR01" H 2200 800 50  0001 C CNN
F 1 "+3.3V" H 2200 1090 50  0000 C CNN
F 2 "" H 2200 950 50  0000 C CNN
F 3 "" H 2200 950 50  0000 C CNN
	1    2200 950 
	1    0    0    -1  
$EndComp
Wire Wire Line
	2300 1500 2400 1500
Connection ~ 2300 2300
Wire Wire Line
	2400 1200 1250 1200
Wire Wire Line
	1250 1300 2400 1300
Wire Wire Line
	1250 1400 2400 1400
Wire Wire Line
	2400 1600 1250 1600
Wire Wire Line
	1250 1700 2400 1700
Wire Wire Line
	1250 1800 2400 1800
Wire Wire Line
	2400 2000 1250 2000
Wire Wire Line
	1250 2100 2400 2100
Wire Wire Line
	1250 2200 2400 2200
Wire Wire Line
	2400 2400 1250 2400
Wire Wire Line
	1250 2500 2400 2500
Wire Wire Line
	1250 2600 2400 2600
Wire Wire Line
	2400 2700 1250 2700
Wire Wire Line
	1250 2800 2400 2800
Wire Wire Line
	1250 2900 2400 2900
Wire Wire Line
	2900 2800 3950 2800
Wire Wire Line
	2900 2900 3950 2900
Wire Wire Line
	2900 2300 3950 2300
Wire Wire Line
	2900 2400 3950 2400
Wire Wire Line
	2900 2100 3950 2100
Wire Wire Line
	2900 2200 3950 2200
Wire Wire Line
	2900 1800 3950 1800
Wire Wire Line
	2900 1900 3950 1900
Wire Wire Line
	2900 1500 3950 1500
Wire Wire Line
	2900 1600 3950 1600
Wire Wire Line
	2900 1400 3950 1400
Wire Wire Line
	2900 2600 3950 2600
Text Label 1250 1200 0    50   ~ 0
GPIO2(SDA1)
Text Label 1250 1300 0    50   ~ 0
GPIO3(SCL1)
Text Label 1250 1400 0    50   ~ 0
GPIO4(GCLK)
Text Label 1250 1600 0    50   ~ 0
GPIO17(GEN0)
Text Label 1250 1700 0    50   ~ 0
GPIO27(GEN2)
Text Label 1250 1800 0    50   ~ 0
GPIO22(GEN3)
Text Label 1250 2000 0    50   ~ 0
GPIO10(SPI0_MOSI)
Text Label 1250 2100 0    50   ~ 0
GPIO9(SPI0_MISO)
Text Label 1250 2200 0    50   ~ 0
GPIO11(SPI0_SCK)
Text Label 1250 2400 0    50   ~ 0
ID_SD
Text Label 1250 2500 0    50   ~ 0
GPIO5
Text Label 1250 2600 0    50   ~ 0
GPIO6
Text Label 1250 2700 0    50   ~ 0
GPIO13(PWM1)
Text Label 1250 2800 0    50   ~ 0
GPIO19(SPI1_MISO)
Text Label 1250 2900 0    50   ~ 0
GPIO26
Text Label 3950 2900 2    50   ~ 0
GPIO20(SPI1_MOSI)
Text Label 3950 2800 2    50   ~ 0
GPIO16
Text Label 3950 2600 2    50   ~ 0
GPIO12(PWM0)
Text Label 3950 2400 2    50   ~ 0
ID_SC
Text Label 3950 2300 2    50   ~ 0
GPIO7(SPI1_CE_N)
Text Label 3950 2200 2    50   ~ 0
GPIO8(SPI0_CE_N)
Text Label 3950 2100 2    50   ~ 0
GPIO25(GEN6)
Text Label 3950 1900 2    50   ~ 0
GPIO24(GEN5)
Text Label 3950 1800 2    50   ~ 0
GPIO23(GEN4)
Text Label 3950 1600 2    50   ~ 0
GPIO18(GEN1)(PWM0)
Text Label 3950 1500 2    50   ~ 0
GPIO15(RXD0)
Text Label 3950 1400 2    50   ~ 0
GPIO14(TXD0)
Wire Wire Line
	3000 1300 2900 1300
Connection ~ 3000 1700
Text Notes 650  7600 0    50   ~ 0
ID_SD and ID_SC PINS:\nThese pins are reserved for HAT ID EEPROM.\n\nAt boot time this I2C interface will be\ninterrogated to look for an EEPROM\nthat identifes the attached board and\nallows automagic setup of the GPIOs\n(and optionally, Linux drivers).\n\nDO NOT USE these pins for anything other\nthan attaching an I2C ID EEPROM. Leave\nunconnected if ID EEPROM not required.
$Comp
L test-rescue:Mounting_Hole-Mechanical MK1
U 1 1 5834FB2E
P 3000 7200
F 0 "MK1" H 3100 7246 50  0000 L CNN
F 1 "M2.5" H 3100 7155 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.7mm_M2.5" H 3000 7200 60  0001 C CNN
F 3 "" H 3000 7200 60  0001 C CNN
	1    3000 7200
	1    0    0    -1  
$EndComp
$Comp
L test-rescue:Mounting_Hole-Mechanical MK3
U 1 1 5834FBEF
P 3450 7200
F 0 "MK3" H 3550 7246 50  0000 L CNN
F 1 "M2.5" H 3550 7155 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.7mm_M2.5" H 3450 7200 60  0001 C CNN
F 3 "" H 3450 7200 60  0001 C CNN
	1    3450 7200
	1    0    0    -1  
$EndComp
$Comp
L test-rescue:Mounting_Hole-Mechanical MK2
U 1 1 5834FC19
P 3000 7400
F 0 "MK2" H 3100 7446 50  0000 L CNN
F 1 "M2.5" H 3100 7355 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.7mm_M2.5" H 3000 7400 60  0001 C CNN
F 3 "" H 3000 7400 60  0001 C CNN
	1    3000 7400
	1    0    0    -1  
$EndComp
$Comp
L test-rescue:Mounting_Hole-Mechanical MK4
U 1 1 5834FC4F
P 3450 7400
F 0 "MK4" H 3550 7446 50  0000 L CNN
F 1 "M2.5" H 3550 7355 50  0000 L CNN
F 2 "MountingHole:MountingHole_2.7mm_M2.5" H 3450 7400 60  0001 C CNN
F 3 "" H 3450 7400 60  0001 C CNN
	1    3450 7400
	1    0    0    -1  
$EndComp
Text Notes 3000 7050 0    50   ~ 0
Mounting Holes
$Comp
L Connector_Generic:Conn_02x20_Odd_Even P1
U 1 1 59AD464A
P 2600 2000
F 0 "P1" H 2650 3117 50  0000 C CNN
F 1 "Conn_02x20_Odd_Even" H 2650 3026 50  0000 C CNN
F 2 "Connector_PinSocket_2.54mm:PinSocket_2x20_P2.54mm_Vertical" H -2250 1050 50  0001 C CNN
F 3 "" H -2250 1050 50  0001 C CNN
	1    2600 2000
	1    0    0    -1  
$EndComp
Wire Wire Line
	2900 3000 3950 3000
Text Label 3950 3000 2    50   ~ 0
GPIO21(SPI1_SCK)
Wire Wire Line
	3100 1100 3100 1200
Wire Wire Line
	3000 2700 3000 3150
Wire Wire Line
	3000 2500 3000 2700
Wire Wire Line
	3000 2000 3000 2500
Wire Wire Line
	2300 3000 2300 3150
Wire Wire Line
	2200 1100 2200 1900
Wire Wire Line
	2300 2300 2300 3000
Wire Wire Line
	3000 1700 3000 2000
Text Label 1250 4700 0    50   ~ 0
GPIO22(GEN3)
Text Label 1250 4800 0    50   ~ 0
GPIO23(GEN4)
Text Label 1250 4900 0    50   ~ 0
GPIO4(GCLK)
Text Label 1250 5000 0    50   ~ 0
GPIO5
Text Label 1250 5100 0    50   ~ 0
GPIO6
Wire Wire Line
	1250 4600 1950 4600
Wire Wire Line
	1250 4700 1950 4700
Wire Wire Line
	1950 4800 1250 4800
Wire Wire Line
	1250 4900 1950 4900
Wire Wire Line
	1950 5000 1250 5000
Wire Wire Line
	1250 5100 1950 5100
Wire Wire Line
	1950 5200 1250 5200
$Comp
L power:GND #PWR04
U 1 1 63694E34
P 2450 5950
F 0 "#PWR04" H 2450 5700 50  0001 C CNN
F 1 "GND" H 2450 5800 50  0000 C CNN
F 2 "" H 2450 5950 50  0000 C CNN
F 3 "" H 2450 5950 50  0000 C CNN
	1    2450 5950
	-1   0    0    -1  
$EndComp
Wire Wire Line
	2450 5800 2450 5950
Wire Wire Line
	2950 5800 2450 5800
Text Label 3750 4500 0    50   ~ 0
GPIO17(GEN0)
Text Label 3750 4600 0    50   ~ 0
GPIO27(GEN2)
Text Label 3750 4700 0    50   ~ 0
GPIO9(SPI0_MISO)
Text Label 3750 4800 0    50   ~ 0
GPIO10(SPI0_MOSI)
Text Label 3750 4900 0    50   ~ 0
GPIO11(SPI0_SCK)
Text Label 3750 5100 0    50   ~ 0
GPIO24(GEN5)
Text Label 3750 5200 0    50   ~ 0
GPIO25(GEN6)
$Comp
L power:GND #PWR08
U 1 1 636C32A8
P 5000 5950
F 0 "#PWR08" H 5000 5700 50  0001 C CNN
F 1 "GND" H 5000 5800 50  0000 C CNN
F 2 "" H 5000 5950 50  0000 C CNN
F 3 "" H 5000 5950 50  0000 C CNN
	1    5000 5950
	-1   0    0    -1  
$EndComp
Wire Wire Line
	4500 5800 5000 5800
Wire Wire Line
	5000 5950 5000 5800
Wire Wire Line
	3750 4500 4500 4500
Wire Wire Line
	4500 4600 3750 4600
Wire Wire Line
	3750 4700 4500 4700
Wire Wire Line
	4500 4800 3750 4800
Wire Wire Line
	3750 4900 4500 4900
Wire Wire Line
	4500 5000 3750 5000
Wire Wire Line
	3750 5100 4500 5100
Wire Wire Line
	4500 5200 3750 5200
$Comp
L power:+5V #PWR07
U 1 1 636DC25B
P 5000 3850
F 0 "#PWR07" H 5000 3700 50  0001 C CNN
F 1 "+5V" H 5000 3990 50  0000 C CNN
F 2 "" H 5000 3850 50  0000 C CNN
F 3 "" H 5000 3850 50  0000 C CNN
	1    5000 3850
	1    0    0    -1  
$EndComp
$Comp
L power:+3.3V #PWR03
U 1 1 636DC265
P 2450 3850
F 0 "#PWR03" H 2450 3700 50  0001 C CNN
F 1 "+3.3V" H 2450 3990 50  0000 C CNN
F 2 "" H 2450 3850 50  0000 C CNN
F 3 "" H 2450 3850 50  0000 C CNN
	1    2450 3850
	1    0    0    -1  
$EndComp
Text GLabel 5650 4500 2    50   Output ~ 0
CLK
Text GLabel 5650 4600 2    50   Output ~ 0
CLR
Wire Wire Line
	5500 4500 5650 4500
Wire Wire Line
	5500 4600 5650 4600
Text GLabel 5650 4700 2    50   Output ~ 0
OE
Text GLabel 5650 4800 2    50   Output ~ 0
CS
Text GLabel 5650 4900 2    50   Output ~ 0
WE
Text GLabel 5650 5000 2    50   Output ~ 0
RST
Text GLabel 5650 5100 2    50   Output ~ 0
EXT0
Text GLabel 5650 5200 2    50   Output ~ 0
EXT1
Wire Wire Line
	5500 4700 5650 4700
Wire Wire Line
	5500 4800 5650 4800
Wire Wire Line
	5650 4900 5500 4900
Wire Wire Line
	5500 5000 5650 5000
Wire Wire Line
	5650 5100 5500 5100
Wire Wire Line
	5500 5200 5650 5200
Entry Wire Line
	4950 1350 5050 1250
Entry Wire Line
	4950 1450 5050 1350
Entry Wire Line
	4950 1550 5050 1450
Entry Wire Line
	4950 1650 5050 1550
Entry Wire Line
	4950 1750 5050 1650
Entry Wire Line
	4950 1850 5050 1750
Entry Wire Line
	4950 1950 5050 1850
Entry Wire Line
	4950 2050 5050 1950
Entry Wire Line
	3050 5200 3150 5100
Entry Wire Line
	3050 5100 3150 5000
Entry Wire Line
	3050 5000 3150 4900
Entry Wire Line
	3050 4900 3150 4800
Entry Wire Line
	3050 4800 3150 4700
Entry Wire Line
	3050 4700 3150 4600
Entry Wire Line
	3050 4600 3150 4500
Entry Wire Line
	3050 4500 3150 4400
Wire Wire Line
	2950 4500 3050 4500
Wire Wire Line
	3050 4600 2950 4600
Wire Wire Line
	2950 4700 3050 4700
Wire Wire Line
	3050 4800 2950 4800
Wire Wire Line
	2950 4900 3050 4900
Wire Wire Line
	3050 5000 2950 5000
Wire Wire Line
	2950 5100 3050 5100
Wire Wire Line
	3050 5200 2950 5200
Text Label 3050 4500 2    50   ~ 0
DA0
Text Label 3050 4600 2    50   ~ 0
DA1
Text Label 3050 4700 2    50   ~ 0
DA2
Text Label 3050 4800 2    50   ~ 0
DA3
Text Label 3050 4900 2    50   ~ 0
DA4
Text Label 3050 5000 2    50   ~ 0
DA5
Text Label 3050 5100 2    50   ~ 0
DA6
Text Label 3050 5200 2    50   ~ 0
DA7
Text Label 5050 1250 0    50   ~ 0
DA0
Text Label 5050 1350 0    50   ~ 0
DA1
Text Label 5050 1450 0    50   ~ 0
DA2
Text Label 5050 1550 0    50   ~ 0
DA3
Text Label 5050 1650 0    50   ~ 0
DA4
Text Label 5050 1750 0    50   ~ 0
DA5
Text Label 5050 1850 0    50   ~ 0
DA6
Text Label 5050 1950 0    50   ~ 0
DA7
$Comp
L power:PWR_FLAG #FLG01
U 1 1 638DC1FF
P 8150 1250
F 0 "#FLG01" H 8150 1325 50  0001 C CNN
F 1 "PWR_FLAG" H 8150 1423 50  0000 C CNN
F 2 "" H 8150 1250 50  0001 C CNN
F 3 "~" H 8150 1250 50  0001 C CNN
	1    8150 1250
	1    0    0    -1  
$EndComp
$Comp
L power:PWR_FLAG #FLG02
U 1 1 638DC7A7
P 8650 1250
F 0 "#FLG02" H 8650 1325 50  0001 C CNN
F 1 "PWR_FLAG" H 8650 1423 50  0000 C CNN
F 2 "" H 8650 1250 50  0001 C CNN
F 3 "~" H 8650 1250 50  0001 C CNN
	1    8650 1250
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR011
U 1 1 638DD25F
P 8150 1450
F 0 "#PWR011" H 8150 1200 50  0001 C CNN
F 1 "GND" H 8155 1277 50  0000 C CNN
F 2 "" H 8150 1450 50  0001 C CNN
F 3 "" H 8150 1450 50  0001 C CNN
	1    8150 1450
	1    0    0    -1  
$EndComp
$Comp
L power:VCC #PWR012
U 1 1 638DE269
P 8650 1450
F 0 "#PWR012" H 8650 1300 50  0001 C CNN
F 1 "VCC" H 8667 1623 50  0000 C CNN
F 2 "" H 8650 1450 50  0001 C CNN
F 3 "" H 8650 1450 50  0001 C CNN
	1    8650 1450
	1    0    0    1   
$EndComp
Wire Wire Line
	8150 1250 8150 1450
Wire Wire Line
	8650 1250 8650 1450
Text Label 1250 5200 0    50   ~ 0
GPIO7(SPI1_CE_N)
$Comp
L 74xx:74HC244 U1
U 1 1 639E5373
P 2450 5000
F 0 "U1" H 2450 5981 50  0000 C CNN
F 1 "74HC244" H 2450 5890 50  0000 C CNN
F 2 "Package_DIP:DIP-20_W7.62mm" H 2450 5000 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/74HC_HCT244.pdf" H 2450 5000 50  0001 C CNN
	1    2450 5000
	-1   0    0    -1  
$EndComp
Wire Wire Line
	2950 5500 2950 5800
Connection ~ 2450 5800
$Comp
L 74xx:74HC244 U2
U 1 1 639E6853
P 5000 5000
F 0 "U2" H 5000 5981 50  0000 C CNN
F 1 "74HC244" H 5000 5890 50  0000 C CNN
F 2 "Package_DIP:DIP-20_W7.62mm" H 5000 5000 50  0001 C CNN
F 3 "https://assets.nexperia.com/documents/data-sheet/74HC_HCT244.pdf" H 5000 5000 50  0001 C CNN
	1    5000 5000
	1    0    0    -1  
$EndComp
Wire Wire Line
	4500 5500 4500 5800
Connection ~ 5000 5800
Wire Wire Line
	2950 5400 2950 5500
Connection ~ 2950 5500
Wire Wire Line
	4500 5400 4500 5500
Connection ~ 4500 5500
Text GLabel 3050 4200 0    50   Input ~ 0
DABUS
Text GLabel 5200 2650 2    50   Output ~ 0
DABUS
Wire Bus Line
	4950 2650 5200 2650
Wire Bus Line
	3050 4200 3150 4200
Wire Wire Line
	6700 1450 6600 1450
Wire Wire Line
	6600 1550 6700 1550
Wire Wire Line
	6700 1650 6600 1650
Wire Wire Line
	6600 1750 6700 1750
Wire Wire Line
	6700 1850 6600 1850
Text GLabel 6600 2050 0    50   BiDi ~ 0
EIO_1
Text GLabel 6600 1950 0    50   BiDi ~ 0
EIO_0
Text GLabel 6600 1650 0    50   Input ~ 0
RST
Text GLabel 6600 1550 0    50   Input ~ 0
WE
Text GLabel 6600 1450 0    50   Input ~ 0
CS
Text GLabel 6600 1350 0    50   Input ~ 0
OE
$Comp
L power:+5V #PWR010
U 1 1 63A04AAD
P 8100 3900
F 0 "#PWR010" H 8100 3750 50  0001 C CNN
F 1 "+5V" H 8100 4040 50  0000 C CNN
F 2 "" H 8100 3900 50  0000 C CNN
F 3 "" H 8100 3900 50  0000 C CNN
	1    8100 3900
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR09
U 1 1 63A05DF0
P 6600 2500
F 0 "#PWR09" H 6600 2250 50  0001 C CNN
F 1 "GND" H 6605 2327 50  0000 C CNN
F 2 "" H 6600 2500 50  0001 C CNN
F 3 "" H 6600 2500 50  0001 C CNN
	1    6600 2500
	1    0    0    -1  
$EndComp
Wire Wire Line
	6600 1250 6700 1250
Wire Wire Line
	6600 2350 6600 2500
Wire Wire Line
	2450 3850 2450 4200
NoConn ~ 3950 1400
NoConn ~ 3950 1500
NoConn ~ 3950 1600
$Comp
L power:PWR_FLAG #FLG03
U 1 1 636F469C
P 9150 1250
F 0 "#FLG03" H 9150 1325 50  0001 C CNN
F 1 "PWR_FLAG" H 9150 1423 50  0000 C CNN
F 2 "" H 9150 1250 50  0001 C CNN
F 3 "~" H 9150 1250 50  0001 C CNN
	1    9150 1250
	1    0    0    -1  
$EndComp
Wire Wire Line
	9150 1250 9150 1450
$Comp
L power:PWR_FLAG #FLG04
U 1 1 636FF5F8
P 9650 1250
F 0 "#FLG04" H 9650 1325 50  0001 C CNN
F 1 "PWR_FLAG" H 9650 1423 50  0000 C CNN
F 2 "" H 9650 1250 50  0001 C CNN
F 3 "~" H 9650 1250 50  0001 C CNN
	1    9650 1250
	1    0    0    -1  
$EndComp
Wire Wire Line
	9650 1250 9650 1450
$Comp
L power:+5V #PWR014
U 1 1 6370A9CD
P 9150 1450
F 0 "#PWR014" H 9150 1300 50  0001 C CNN
F 1 "+5V" H 9150 1590 50  0000 C CNN
F 2 "" H 9150 1450 50  0000 C CNN
F 3 "" H 9150 1450 50  0000 C CNN
	1    9150 1450
	-1   0    0    1   
$EndComp
$Comp
L power:+3.3V #PWR015
U 1 1 6370A9D7
P 9650 1450
F 0 "#PWR015" H 9650 1300 50  0001 C CNN
F 1 "+3.3V" H 9650 1590 50  0000 C CNN
F 2 "" H 9650 1450 50  0000 C CNN
F 3 "" H 9650 1450 50  0000 C CNN
	1    9650 1450
	-1   0    0    1   
$EndComp
NoConn ~ 3950 2800
NoConn ~ 1250 2900
Wire Wire Line
	1250 4500 1950 4500
Text Label 8650 4500 2    50   ~ 0
GPIO12(PWM0)
$Comp
L Jumper:SolderJumper_3_Open JP1
U 1 1 637F6150
P 8550 2400
F 0 "JP1" H 8550 2513 50  0000 C CNN
F 1 "SolderJumper_3_Open" H 8550 2604 50  0000 C CNN
F 2 "Jumper:SolderJumper-3_P1.3mm_Open_RoundedPad1.0x1.5mm_NumberLabels" H 8550 2400 50  0001 C CNN
F 3 "~" H 8550 2400 50  0001 C CNN
	1    8550 2400
	-1   0    0    1   
$EndComp
$Comp
L Jumper:SolderJumper_3_Open JP2
U 1 1 638416D2
P 8550 3250
F 0 "JP2" H 8550 3363 50  0000 C CNN
F 1 "SolderJumper_3_Open" H 8550 3454 50  0000 C CNN
F 2 "Jumper:SolderJumper-3_P1.3mm_Open_RoundedPad1.0x1.5mm_NumberLabels" H 8550 3250 50  0001 C CNN
F 3 "~" H 8550 3250 50  0001 C CNN
	1    8550 3250
	-1   0    0    1   
$EndComp
Wire Wire Line
	8550 2100 8550 2250
Wire Wire Line
	8750 2400 8900 2400
Wire Wire Line
	8200 2400 8350 2400
Wire Wire Line
	8200 3250 8350 3250
Wire Wire Line
	8550 2950 8550 3100
Text GLabel 6600 1250 0    50   Input ~ 0
PWR
Text GLabel 8250 4100 2    50   Output ~ 0
PWR
Wire Wire Line
	8100 3900 8100 4100
Wire Wire Line
	8100 4100 8250 4100
Wire Wire Line
	8750 3250 8900 3250
Text Label 8650 4700 2    50   ~ 0
GPIO13(PWM1)
Wire Wire Line
	8550 2100 8600 2100
Wire Wire Line
	8550 2950 8600 2950
Wire Wire Line
	6600 1350 6700 1350
$Comp
L Connector:Conn_01x12_Male J2
U 1 1 639D4CB5
P 6900 1750
F 0 "J2" H 7000 2500 50  0000 C CNN
F 1 "Conn_01x12_Male" H 7000 2400 50  0000 C CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x12_P2.54mm_Vertical" H 6900 1750 50  0001 C CNN
F 3 "~" H 6900 1750 50  0001 C CNN
	1    6900 1750
	-1   0    0    -1  
$EndComp
Wire Wire Line
	6600 2350 6700 2350
Wire Wire Line
	6600 1950 6700 1950
Wire Wire Line
	6700 2050 6600 2050
Wire Wire Line
	6700 2150 6600 2150
Wire Wire Line
	6700 2250 6600 2250
Text GLabel 8850 4100 2    50   Output ~ 0
PWR3
Wire Wire Line
	8700 3900 8700 4100
Wire Wire Line
	8700 4100 8850 4100
$Comp
L power:+3.3V #PWR013
U 1 1 63A8F20A
P 8700 3900
F 0 "#PWR013" H 8700 3750 50  0001 C CNN
F 1 "+3.3V" H 8700 4040 50  0000 C CNN
F 2 "" H 8700 3900 50  0000 C CNN
F 3 "" H 8700 3900 50  0000 C CNN
	1    8700 3900
	1    0    0    -1  
$EndComp
Text Label 3750 5000 0    50   ~ 0
GPIO19(SPI1_MISO)
Text Label 1250 4500 0    50   ~ 0
GPIO20(SPI1_MOSI)
Text Label 1250 4600 0    50   ~ 0
GPIO21(SPI1_SCK)
Text GLabel 8600 2950 2    50   BiDi ~ 0
EIO_1
Text GLabel 8600 2100 2    50   BiDi ~ 0
EIO_0
Text GLabel 8200 2400 0    50   Input ~ 0
EXT0
Text GLabel 8200 3250 0    50   Input ~ 0
EXT1
Text GLabel 6600 2150 0    50   Input ~ 0
PWR3
Text Label 8900 2400 0    50   ~ 0
GPIO2(SDA1)
Text Label 8900 3250 0    50   ~ 0
GPIO3(SCL1)
Text GLabel 8850 4700 2    50   Output ~ 0
PWM1
Wire Wire Line
	8650 4700 8850 4700
Wire Wire Line
	8650 4500 8850 4500
Text GLabel 8850 4500 2    50   Output ~ 0
PWM0
Text GLabel 5300 2050 0    50   Input ~ 0
PWM0
Text GLabel 5300 2150 0    50   Input ~ 0
PWM1
Text GLabel 6600 2250 0    50   BiDi ~ 0
EIO_2
Text Label 8650 4900 2    50   ~ 0
GPIO8(SPI0_CE_N)
Text GLabel 8850 4900 2    50   BiDi ~ 0
EIO_2
Wire Wire Line
	8650 4900 8850 4900
NoConn ~ 3950 2400
NoConn ~ 1250 2400
Wire Wire Line
	5000 3850 5000 4200
Text GLabel 6600 1750 0    50   Input ~ 0
CLK
Text GLabel 6600 1850 0    50   Input ~ 0
CLR
Wire Wire Line
	5400 2050 5300 2050
Wire Wire Line
	5050 1950 5400 1950
Wire Wire Line
	5050 1850 5400 1850
Wire Wire Line
	5050 1750 5400 1750
Wire Wire Line
	5050 1650 5400 1650
Wire Wire Line
	5050 1550 5400 1550
Wire Wire Line
	5050 1450 5400 1450
Wire Wire Line
	5050 1350 5400 1350
Wire Wire Line
	5400 2150 5300 2150
Wire Wire Line
	5050 1250 5400 1250
$Comp
L Connector:Conn_01x10_Male J1
U 1 1 63733EA3
P 5600 1650
F 0 "J1" H 5750 2300 50  0000 R CNN
F 1 "Conn_01x10_Male" H 6050 2200 50  0000 R CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x10_P2.54mm_Vertical" H 5600 1650 50  0001 C CNN
F 3 "~" H 5600 1650 50  0001 C CNN
	1    5600 1650
	-1   0    0    -1  
$EndComp
Wire Bus Line
	3150 4200 3150 5100
Wire Bus Line
	4950 1350 4950 2650
$EndSCHEMATC
