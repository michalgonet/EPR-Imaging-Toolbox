#DESC	1.2 * DESCRIPTOR INFORMATION ***********************
*
*	Dataset Type and Format:
*
DSRC	EXP
BSEQ	BIG
IKKF	REAL
XTYP	IDX
YTYP	IGD
ZTYP	NODATA
*
*	Item Formats:
*
IRFMT	D
YFMT	D
*
*	Data Ranges and Resolutions:
*
XPTS	256
XMIN	385.500000
XWID	5.976562
YPTS	400
YMIN	1.000000
YWID	399.000000
*
*	Documentational Text:
*
TITL	'20x20'
IRNAM	'Intensity'
XNAM	'Field'
YNAM	'Angle'
IRUNI	''
XUNI	'G'
YUNI	''
*
************************************************************
*
#SPL	1.2 * STANDARD PARAMETER LAYER
*
OPER    xuser
DATE    10/10/16
TIME    19:01:08
CMNT    
SAMP    
SFOR    
STAG    C
EXPT    CWIMG
OXS1    IADC
AXS1    B0VL
AXS2    GRAD
AXS3    
A1CT    0.03885
A1SW    0.0006
MWFQ    1.106112e+09
IMGP    0.000
IMGT    0.000
GRAD    1.500
IMTY    3D
MWPW    0.000854
A2RS    400
A2LL    1
A2SW    1
AVGS    1
SPTP    0.00128
RCAG    30
RCHM    1
B0MA    1e-05
B0MF    30000
RCPH    0.0
RCOF    0.0
A1RS    256
RCTC    0
*
************************************************************
*
#DSL	1.0 * DEVICE SPECIFIC LAYER
*

.DVC     acqStart, 1.0


.DVC     fieldCtrl, 1.0

AllegroMode        True
CenterField        388.50 G
Delay              0.0 s
FieldFlyback       On
FieldWait          Wait LED off
GFactor            2.000000
MeasuringHall      False
SetToSampleG       False
StaticFieldMon     385.500 G
SweepDirection     Up
SweepWidth         6.0 G
WidthTM            200.0 G

.DVC     fieldSweep, 1.0


.DVC     freqCounter, 1.0

FrequencyMon       1.106112 GHz
QMonitBridge       On

.DVC     grdUnit, 1.0

AnglePhi           0.000 deg
AnglePsi           1.5000 G/cm
AngleTheta         0.000 deg
BandWidth          0.015 G
CurrentCheck       Wait stable
CurrentStrMon      1.500 G/cm
EnableStatic       False
FieldOfView        0.80 mm
FirstAlpha         4.500 deg
ImageOrient        XY
ImageType          3D
MaxPsi             0.00 deg
MinSW              10.21 G
NPixel             8
NrOfAlpha          20
NrOfBeta           20
NrOfProfs          400
NrOfPsi            1
PixelSize          0.1000 mm
SWTime             0.328 s
SleepSecs          0.0 s
SpecWidth          5.000 G
SpectralRes        0.62500 G/p
TotalTime          18.0 min

.DVC     mwBridge, 1.0

AcqFineTuning      Each Slice Scan
Power              0.8540 mW
PowerAtten         26.00 dB

.DVC     ramp2, 1.0

Flyback            False
NbCycles           1
NbPoints           400
StartValue         1
SweepData          
SweepWidth         1
sweepType          Ramp up

.DVC     recorder, 1.0

BaselineCorr       On
NbScansAcc         1
NbScansDone        1
NbScansToDo        1
ReplaceMode        On
SmoothMode         Manual
SmoothPoints       1

.DVC     scanEnd, 1.0


.DVC     signalChannel, 1.0

AFCTrap            True
AllegroMode        True
AllowShortCt       False
Calibrated         True
ConvTime           1.28 ms
DModDetectSCT      First
DualDetect         OFF
EliDelay           1.0 us
Enable1stHarm      True
Enable1stHarm90    False
Enable2ndHarm      False
Enable2ndHarm90    False
Enable3rdHarm      False
Enable3rdHarm90    False
Enable4thHarm      False
Enable4thHarm90    False
Enable5thHarm      False
Enable5thHarm90    False
EnableDisp         False
EnableImag         Disable
ExtLockIn          False
ExtTrigger         False
Gain               30 dB
GainB              30 dB
Harmonic           1
HighPass           True
InputPlugA         AC3
InputPlugB         AC3
Integrator         False
IsCalibExp         False
ModAmp             0.100 G
ModFreq            30.00 kHz
ModPhase           0.0
Offset             0.0 %
QuadMode           False
Resolution         256
Resonator          1
SctNorm            True
SctRevision        Allegro
SetAllOrd          False
SetOrdDef          False
SpuExtension       True
SpuRevision        MultiHarmonic
SweepTime          0.32762 s
TimeConst          0
TimeExp            False
TuneCaps           0

*
************************************************************
