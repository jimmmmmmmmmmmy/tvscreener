```python
import tvscreener as tvs
from tvscreener.filter import Country
from tvscreener import TimeInterval
import pandas as pd

%load_ext autoreload
%autoreload 2

```


```python
# Initialize the StockScreener with your session credentials
screener = tvs.StockScreener(sessionid="YOUR SESSION ID", sessionid_sign="YOUR SESSION ID SIGN")

if screener.is_authenticated():
    print("Successfully authenticated with TradingView")
else:
    print("Failed to authenticate with TradingView")

# Set the country filter to China
screener.set_countries(Country.CHINA)

# Get all the data
df = screener.get()

# Check if the DataFrame is empty
if df.empty:
    print("No data found")
else:
    # Define desired columns and their new names
    desired_columns = {
        'Symbol': 'Symbol',
        'Name': 'Name',
        'close': 'Price',
        'Change from Open %' : 'Change from Open %',
        'Country' : 'Country'
    }

    # Format the data (only for columns that exist)
    for col in df_selected.columns:
        if col == 'Price' or col == 'Change %' or col == 'P/E Ratio' or col == 'Dividend Yield %':
            df_selected[col] = df_selected[col].round(2)
        elif col == 'Volume':
            df_selected[col] = df_selected[col].apply(lambda x: f'{x:,.0f}' if pd.notnull(x) else '')
        elif col == 'Market Cap':
            df_selected[col] = df_selected[col].apply(lambda x: f'${x/1e9:.2f}B' if x >= 1e9 else f'${x/1e6:.2f}M' if pd.notnull(x) else '')

    # Sort by Changre from Open % if available, otherwise by the first column
    sort_column = 'Change from Open %' if 'Change from Open %' in df_selected.columns else df_selected.columns[0]
    df_sorted = df_selected.sort_values(sort_column, ascending=False)

    # Display the results
    print("\nTop Chinese Stocks:")
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    print(df_sorted)

    # Print the number of results
    print(f"\nTotal number of Chinese stocks: {len(df_sorted)}")
```

    Successfully authenticated with TradingView
    
    Top Chinese Stocks:
               Symbol   Name  Change from Open % Country
    245   NASDAQ:CHSN   CHSN          428.928571   China
    430      OTC:YBCN   YBCN          222.580645   China
    461     OTC:SECOY  SECOY          100.000000   China
    473      OTC:ZHUD   ZHUD           50.000000   China
    404      OTC:DRCR   DRCR           44.124169   China
    229      OTC:EUBG   EUBG           38.950000   China
    427       AMEX:BQ     BQ           34.717391   China
    195   NASDAQ:UXIN   UXIN           31.484794   China
    146     OTC:TSYHF  TSYHF           28.874269   China
    359      OTC:HERB   HERB           23.505976   China
    448     OTC:QTTOY  QTTOY           23.157895   China
    315   NASDAQ:AIXI   AIXI           19.469027   China
    425   NASDAQ:TAOP   TAOP           19.402985   China
    283     NYSE:OCFT   OCFT           18.992248   China
    232   NASDAQ:DOGZ   DOGZ           18.800421   China
    306     NASDAQ:NA     NA           18.733154   China
    190     OTC:CTRYY  CTRYY           17.674419   China
    198     NASDAQ:EH     EH           16.411960   China
    379   NASDAQ:PETZ   PETZ           16.153846   China
    298   NASDAQ:NISN   NISN           15.008626   China
    313     NASDAQ:JG     JG           14.077670   China
    293     NASDAQ:YI     YI           14.021858   China
    426     NASDAQ:TC     TC           13.756614   China
    286   NASDAQ:WIMI   WIMI           13.402062   China
    390   NASDAQ:STEC   STEC           12.959811   China
    260    NASDAQ:QSG    QSG           12.727273   China
    472     OTC:ZKGCF  ZKGCF           12.500000   China
    193      NYSE:JKS    JKS           11.925234   China
    226      OTC:LNMG   LNMG           11.111111   China
    415   NASDAQ:ATXG   ATXG           11.055413   China
    20      OTC:XIACF  XIACF           10.175439   China
    261   NASDAQ:BZUN   BZUN            9.610390   China
    389   NASDAQ:KRKR   KRKR            9.505859   China
    361    NASDAQ:DSY    DSY            9.375000   China
    207    NASDAQ:FLX    FLX            9.151515   China
    254     NYSE:LANV   LANV            9.126984   China
    335    NASDAQ:JFU    JFU            8.984375   China
    235       NYSE:ZH     ZH            8.843537   China
    127     OTC:GNENF  GNENF            8.350694   China
    194     NYSE:HUYA   HUYA            8.347826   China
    191       NYSE:DQ     DQ            8.031774   China
    392    NASDAQ:HAO    HAO            7.153558   China
    322   NASDAQ:HUIZ   HUIZ            7.046230   China
    333   NASDAQ:GDHG   GDHG            6.910569   China
    179     NASDAQ:WB     WB            6.880734   China
    288    NASDAQ:LSB    LSB            6.653620   China
    321   NASDAQ:RCON   RCON            6.574394   China
    391   NASDAQ:GURE   GURE            6.476400   China
    52      OTC:KSHTY  KSHTY            6.382979   China
    241    NASDAQ:RTC    RTC            6.280193   China
    269     NYSE:CMCM   CMCM            6.222222   China
    451     OTC:DXFFY  DXFFY            6.060606   China
    449      OTC:SPOM   SPOM            5.882353   China
    180   NASDAQ:ZLAB   ZLAB            5.397841   China
    79      OTC:CHVKY  CHVKY            5.294379   China
    70      OTC:ZTCOF  ZTCOF            5.263158   China
    280       NYSE:IH     IH            5.164319   China
    64      OTC:DIDIY  DIDIY            4.831933   China
    187     OTC:BJCHY  BJCHY            4.573783   China
    353     OTC:PAIYY  PAIYY            4.545455   China
    225     OTC:EVGRF  EVGRF            4.255319   China
    304    NASDAQ:AZI    AZI            4.210526   China
    366      NYSE:SOS    SOS            4.190785   China
    374     NASDAQ:QH     QH            4.137931   China
    247    NASDAQ:ZJK    ZJK            4.012814   China
    112     OTC:MLLUY  MLLUY            3.987885   China
    384     NASDAQ:YJ     YJ            3.982301   China
    405    NASDAQ:OST    OST            3.974730   China
    285   NASDAQ:SFWL   SFWL            3.875969   China
    302   NASDAQ:LICN   LICN            3.763441   China
    199   NASDAQ:VNET   VNET            3.694581   China
    336    NASDAQ:CHR    CHR            3.630363   China
    355   NASDAQ:BHAT   BHAT            3.613445   China
    338    NASDAQ:IZM    IZM            3.508772   China
    326     NYSE:FENG   FENG            3.481013   China
    284   NASDAQ:CBAT   CBAT            3.389831   China
    157    NASDAQ:GDS    GDS            3.362915   China
    219      NYSE:ZKH    ZKH            3.342618   China
    156     OTC:UPCHY  UPCHY            3.285439   China
    15      OTC:CILJF  CILJF            3.196347   China
    330   NASDAQ:ABLV   ABLV            3.181818   China
    227      NYSE:WDH    WDH            3.125000   China
    350   NASDAQ:UCAR   UCAR            3.104037   China
    341   NASDAQ:UTSI   UTSI            3.103448   China
    141     NYSE:MNSO   MNSO            2.997003   China
    82      OTC:AIRYY  AIRYY            2.961276   China
    433    NASDAQ:WNW    WNW            2.909091   China
    117     OTC:XNGSY  XNGSY            2.862720   China
    186     OTC:PANHF  PANHF            2.844444   China
    5       OTC:IDCBY  IDCBY            2.761506   China
    215     NYSE:RERE   RERE            2.749141   China
    230       NYSE:QD     QD            2.690583   China
    104      NYSE:YMM    YMM            2.556237   China
    66      OTC:WUXAY  WUXAY            2.539759   China
    421   NASDAQ:BAOS   BAOS            2.523086   China
    224     OTC:SIOLY  SIOLY            2.500000   China
    243   NASDAQ:DOYU   DOYU            2.488038   China
    1       OTC:TCTZF  TCTZF            2.474576   China
    401   NASDAQ:CREG   CREG            2.439024   China
    54      NYSE:BEKE   BEKE            2.380952   China
    346     NYSE:FEDU   FEDU            2.344008   China
    100     NYSE:XPEV   XPEV            2.316294   China
    189     NYSE:FINV   FINV            2.308802   China
    131     OTC:LKNCY  LKNCY            2.275190   China
    220   NASDAQ:DADA   DADA            2.262443   China
    96      OTC:TSGTY  TSGTY            2.229222   China
    272   NASDAQ:XNET   XNET            2.102804   China
    91      OTC:HDALF  HDALF            2.083333   China
    107     OTC:CSPCY  CSPCY            2.071006   China
    216      NYSE:DAO    DAO            2.048417   China
    145   NASDAQ:QFIN   QFIN            1.999385   China
    111     OTC:JEXYF  JEXYF            1.904762   China
    84      OTC:CLPXY  CLPXY            1.774194   China
    116     OTC:JEXYY  JEXYY            1.744043   China
    436   NASDAQ:SXTC   SXTC            1.697313   China
    212     NYSE:NOAH   NOAH            1.691007   China
    409   NASDAQ:LKCO   LKCO            1.654412   China
    418   NASDAQ:CNET   CNET            1.652893   China
    402    NASDAQ:BON    BON            1.651842   China
    351   NASDAQ:HKIT   HKIT            1.639344   China
    74      NYSE:YUMC   YUMC            1.633065   China
    31      NASDAQ:JD     JD            1.490925   China
    214   NASDAQ:HSAI   HSAI            1.320755   China
    126     NASDAQ:BZ     BZ            1.319958   China
    301   NASDAQ:CASI   CASI            1.282051   China
    23      OTC:BYDDF  BYDDF            1.246753   China
    310   NASDAQ:NCTY   NCTY            1.223047   China
    256   NASDAQ:NWGL   NWGL            1.206940   China
    77    NASDAQ:BILI   BILI            1.137197   China
    317     NYSE:BEST   BEST            1.111111   China
    324     NASDAQ:SJ     SJ            1.000000   China
    265    NASDAQ:AHG    AHG            0.900901   China
    240      NYSE:YSG    YSG            0.867052   China
    270   NASDAQ:CAAS   CAAS            0.858369   China
    277     NASDAQ:SY     SY            0.825000   China
    4       OTC:MPNGF  MPNGF            0.818452   China
    106     OTC:WXIBF  WXIBF            0.806452   China
    22      OTC:BYDDY  BYDDY            0.777303   China
    318   NASDAQ:NAAS   NAAS            0.750000   China
    94       NYSE:NIO    NIO            0.744048   China
    142     OTC:LNNGY  LNNGY            0.707819   China
    412   NASDAQ:ANTE   ANTE            0.680643   China
    434      AMEX:ITP    ITP            0.659224   China
    196   NASDAQ:MOMO   MOMO            0.651042   China
    17      OTC:CIHKY  CIHKY            0.644068   China
    101     OTC:WXXWY  WXXWY            0.553506   China
    203     NYSE:TUYA   TUYA            0.546448   China
    258     NYSE:CANG   CANG            0.543478   China
    43      OTC:HSHCY  HSHCY            0.527742   China
    394   NASDAQ:WAFU   WAFU            0.402010   China
    287     OTC:JWCTF  JWCTF            0.354191   China
    26      OTC:SNPMF  SNPMF            0.325632   China
    163   NASDAQ:ATAT   ATAT            0.323741   China
    123     OTC:SOTGY  SOTGY            0.258231   China
    311     NYSE:ZEPP   ZEPP            0.257732   China
    279      NYSE:SRL    SRL            0.243700   China
    110     NYSE:VIPS   VIPS            0.229885   China
    11      OTC:CICHY  CICHY            0.225153   China
    16      OTC:PNGAY  PNGAY            0.204360   China
    267      OTC:LDDD   LDDD            0.200401   China
    60      OTC:CMCLF  CMCLF            0.190476   China
    49      OTC:CTPCY  CTPCY            0.156986   China
    124     OTC:AKESF  AKESF            0.153296   China
    8       OTC:ACGBY  ACGBY            0.147481   China
    339      NYSE:CCM    CCM            0.117986   China
    292   NASDAQ:GLAC   GLAC            0.095329   China
    150     OTC:XISHY  XISHY            0.090868   China
    7       OTC:BABAF  BABAF            0.070771   China
    319      OTC:LNBY   LNBY            0.000000   China
    386   NASDAQ:JXJT   JXJT            0.000000   China
    382     OTC:AIJTY  AIJTY            0.000000   China
    316  NASDAQ:FVNNU  FVNNU            0.000000   China
    208     OTC:GRMHF  GRMHF            0.000000   China
    209     OTC:SHPHF  SHPHF            0.000000   China
    314     OTC:SFUNY  SFUNY            0.000000   China
    271      OTC:FVTI   FVTI            0.000000   China
    380      OTC:SVMB   SVMB            0.000000   China
    221     OTC:SIOLF  SIOLF            0.000000   China
    347   NASDAQ:EPOW   EPOW            0.000000   China
    276      OTC:DYNA   DYNA            0.000000   China
    268     OTC:HUMDF  HUMDF            0.000000   China
    264     OTC:TMPPF  TMPPF            0.000000   China
    263     OTC:JUTOY  JUTOY            0.000000   China
    352   NASDAQ:ZKIN   ZKIN            0.000000   China
    354   NASDAQ:WETH   WETH            0.000000   China
    344   NASDAQ:MHUA   MHUA            0.000000   China
    253     OTC:ATONY  ATONY            0.000000   China
    250     OTC:CSCHF  CSCHF            0.000000   China
    249     OTC:EGRNF  EGRNF            0.000000   China
    248     OTC:VBIZF  VBIZF            0.000000   China
    246     OTC:MROPF  MROPF            0.000000   China
    362      OTC:SRRE   SRRE            0.000000   China
    365     NYSE:MOGU   MOGU            0.000000   China
    297     OTC:NTPIF  NTPIF            0.000000   China
    368      OTC:JRSS   JRSS            0.000000   China
    369   NASDAQ:EDTK   EDTK            0.000000   China
    300      OTC:ELRE   ELRE            0.000000   China
    234      OTC:SCGY   SCGY            0.000000   China
    233     OTC:GRVWF  GRVWF            0.000000   China
    303   NASDAQ:DIST   DIST            0.000000   China
    307      OTC:EZOO   EZOO            0.000000   China
    308      OTC:KPEA   KPEA            0.000000   China
    228     OTC:BEIJF  BEIJF            0.000000   China
    323      OTC:LEIC   LEIC            0.000000   China
    222     OTC:YHEKF  YHEKF            0.000000   China
    238     OTC:CMEIF  CMEIF            0.000000   China
    410     OTC:ZHGWF  ZHGWF            0.000000   China
    204     OTC:WCHNF  WCHNF            0.000000   China
    200     OTC:GZUHY  GZUHY            0.000000   China
    46      OTC:PPCCY  PPCCY            0.000000   China
    463     OTC:MKDTY  MKDTY            0.000000   China
    462      OTC:HHBT   HHBT            0.000000   China
    50      OTC:ANPDF  ANPDF            0.000000   China
    53      OTC:KUASF  KUASF            0.000000   China
    55      OTC:CICOF  CICOF            0.000000   China
    56      OTC:CTPCF  CTPCF            0.000000   China
    57      OTC:GWLLY  GWLLY            0.000000   China
    460      OTC:AAPT   AAPT            0.000000   China
    459      OTC:CHGS   CHGS            0.000000   China
    61      OTC:CCOZY  CCOZY            0.000000   China
    458     OTC:RAHGF  RAHGF            0.000000   China
    457      OTC:CMFO   CMFO            0.000000   China
    456      OTC:EVKG   EVKG            0.000000   China
    67      OTC:CRWOF  CRWOF            0.000000   China
    455      OTC:CNCT   CNCT            0.000000   China
    454      OTC:GGEI   GGEI            0.000000   China
    71      OTC:ALMMF  ALMMF            0.000000   China
    72      OTC:YZCHF  YZCHF            0.000000   China
    452     OTC:CTKYY  CTKYY            0.000000   China
    76      OTC:AHCHF  AHCHF            0.000000   China
    81      OTC:CLPXF  CLPXF            0.000000   China
    83      OTC:CHHQF  CHHQF            0.000000   China
    85      OTC:AICAF  AICAF            0.000000   China
    86      OTC:CHKIF  CHKIF            0.000000   China
    464     OTC:MFLTY  MFLTY            0.000000   China
    465     OTC:WEIDY  WEIDY            0.000000   China
    42      OTC:HRSHF  HRSHF            0.000000   China
    470      OTC:ZSTN   ZSTN            0.000000   China
    475      OTC:TNMD   TNMD            0.000000   China
    3       OTC:IDCBF  IDCBF            0.000000   China
    474      OTC:YCQH   YCQH            0.000000   China
    10      OTC:ACGBF  ACGBF            0.000000   China
    12      OTC:CICHF  CICHF            0.000000   China
    14      OTC:BACHF  BACHF            0.000000   China
    18      OTC:PIAIF  PIAIF            0.000000   China
    19      OTC:XIACY  XIACY            0.000000   China
    21      OTC:CIHHF  CIHHF            0.000000   China
    471     OTC:TANAF  TANAF            0.000000   China
    25      OTC:CUAEF  CUAEF            0.000000   China
    28      OTC:BCMXY  BCMXY            0.000000   China
    466     OTC:JRJCY  JRJCY            0.000000   China
    29      OTC:BKFCF  BKFCF            0.000000   China
    30      OTC:ZIJMY  ZIJMY            0.000000   China
    32      OTC:ZIJMF  ZIJMF            0.000000   China
    33      OTC:NETTF  NETTF            0.000000   China
    469      OTC:QING   QING            0.000000   China
    35      OTC:JDCMF  JDCMF            0.000000   China
    36      OTC:PSTVY  PSTVY            0.000000   China
    37      OTC:PSBKF  PSBKF            0.000000   China
    468     OTC:CHNGQ  CHNGQ            0.000000   China
    39      OTC:CHCJY  CHCJY            0.000000   China
    467      OTC:PUDA   PUDA            0.000000   China
    447      OTC:HGYN   HGYN            0.000000   China
    88      OTC:SZHIF  SZHIF            0.000000   China
    89      OTC:HUNGF  HUNGF            0.000000   China
    147     OTC:AACAF  AACAF            0.000000   China
    149     OTC:XJNGF  XJNGF            0.000000   China
    419      OTC:TGGI   TGGI            0.000000   China
    152     OTC:XNYIF  XNYIF            0.000000   China
    153     OTC:SNOTF  SNOTF            0.000000   China
    155     OTC:ZSHGY  ZSHGY            0.000000   China
    162     OTC:ZHEXF  ZHEXF            0.000000   China
    164     OTC:UNPSF  UNPSF            0.000000   China
    165     OTC:SHWGY  SHWGY            0.000000   China
    167     OTC:SPTJF  SPTJF            0.000000   China
    169    NASDAQ:LOT    LOT            0.000000   China
    170     OTC:CGSHY  CGSHY            0.000000   China
    171     NASDAQ:IQ     IQ            0.000000   China
    172     OTC:DNFGY  DNFGY            0.000000   China
    173     OTC:SENGF  SENGF            0.000000   China
    174     OTC:DNFGF  DNFGF            0.000000   China
    175     OTC:GNGYF  GNGYF            0.000000   China
    403      OTC:AIXN   AIXN            0.000000   China
    177     OTC:KGDEF  KGDEF            0.000000   China
    182     OTC:SURRY  SURRY            0.000000   China
    183     OTC:SEXHF  SEXHF            0.000000   China
    184     OTC:MCRPF  MCRPF            0.000000   China
    185     OTC:XTEPY  XTEPY            0.000000   China
    188     OTC:CFTLF  CFTLF            0.000000   China
    192     OTC:CIMEF  CIMEF            0.000000   China
    197     OTC:DPCDF  DPCDF            0.000000   China
    148     OTC:KGDEY  KGDEY            0.000000   China
    144     OTC:FOSUY  FOSUY            0.000000   China
    442      OTC:CSOL   CSOL            0.000000   China
    143     OTC:LNNGF  LNNGF            0.000000   China
    441     OTC:BETSF  BETSF            0.000000   China
    93      OTC:HAITY  HAITY            0.000000   China
    95      OTC:NIOIF  NIOIF            0.000000   China
    98      OTC:TSGTF  TSGTF            0.000000   China
    99      OTC:CHEAF  CHEAF            0.000000   China
    102     OTC:XPNGF  XPNGF            0.000000   China
    103     OTC:SHHGF  SHHGF            0.000000   China
    105     OTC:GNZUF  GNZUF            0.000000   China
    108     OTC:BYDIY  BYDIY            0.000000   China
    109     OTC:IVBXF  IVBXF            0.000000   China
    113     OTC:BYDIF  BYDIF            0.000000   China
    435     OTC:RAASY  RAASY            0.000000   China
    320     OTC:KNTPF  KNTPF            0.000000   China
    118     OTC:ZLIOY  ZLIOY            0.000000   China
    119     OTC:YSHLF  YSHLF            0.000000   China
    121     OTC:XNGSF  XNGSF            0.000000   China
    122     OTC:CRYCY  CRYCY            0.000000   China
    128     OTC:SHPMF  SHPMF            0.000000   China
    130     OTC:CHOLF  CHOLF            0.000000   China
    132     OTC:SNTMF  SNTMF            0.000000   China
    135     OTC:CCGDF  CCGDF            0.000000   China
    136     OTC:CFEIY  CFEIY            0.000000   China
    137     OTC:CHFLF  CHFLF            0.000000   China
    138     OTC:CSDXF  CSDXF            0.000000   China
    420     OTC:FHSEY  FHSEY            0.000000   China
    345   NASDAQ:RETO   RETO           -0.007518   China
    0       OTC:TCEHY  TCEHY           -0.032900   China
    73      OTC:BLBLF  BLBLF           -0.033501   China
    68       NYSE:ZTO    ZTO           -0.037037   China
    373   NASDAQ:JDZG   JDZG           -0.046476   China
    210     OTC:TSIOF  TSIOF           -0.047159   China
    58      OTC:GWLLF  GWLLF           -0.048900   China
    75      OTC:AHCHY  AHCHY           -0.093809   China
    120     OTC:TYCMY  TYCMY           -0.104393   China
    24      OTC:CSUAY  CSUAY           -0.106952   China
    97      OTC:SHZHY  SHZHY           -0.115473   China
    160     OTC:HEGIY  HEGIY           -0.142898   China
    364   NASDAQ:ZCMD   ZCMD           -0.202429   China
    161     OTC:HEGIF  HEGIF           -0.203540   China
    59      NASDAQ:LI     LI           -0.221465   China
    63      OTC:CMAKY  CMAKY           -0.224719   China
    13      OTC:BACHY  BACHY           -0.243309   China
    218     NASDAQ:LX     LX           -0.273973   China
    328   NASDAQ:CDTG   CDTG           -0.274725   China
    114     OTC:SHTDY  SHTDY           -0.277008   China
    223   NASDAQ:SOHU   SOHU           -0.292398   China
    159     OTC:CBUMY  CBUMY           -0.342508   China
    151     OTC:AACAY  AACAY           -0.365854   China
    176     OTC:SHZNF  SHZNF           -0.379210   China
    154     OTC:TSYHY  TSYHY           -0.380025   China
    168     OTC:ZZHGY  ZZHGY           -0.425532   China
    2       OTC:MPNGY  MPNGY           -0.458295   China
    48      OTC:ANPDY  ANPDY           -0.502939   China
    211     OTC:SOLLY  SOLLY           -0.503356   China
    476   NASDAQ:ZBAO   ZBAO           -0.510204   China
    417   NASDAQ:TIRX   TIRX           -0.515464   China
    34    NASDAQ:NTES   NTES           -0.650485   China
    342   NASDAQ:MTEN   MTEN           -0.666667   China
    327   NASDAQ:EBON   EBON           -0.667780   China
    242      NYSE:XYF    XYF           -0.821622   China
    399   NASDAQ:SISI   SISI           -0.847080   China
    44    NASDAQ:BIDU   BIDU           -0.861605   China
    413    NASDAQ:UPC    UPC           -0.954545   China
    6       NYSE:BABA   BABA           -0.981282   China
    205     NYSE:GOTU   GOTU           -1.010101   China
    213      NYSE:DDL    DDL           -1.049869   China
    329    NASDAQ:BNR    BNR           -1.066667   China
    92    NASDAQ:HTHT   HTHT           -1.137171   China
    69      OTC:YZCAY  YZCAY           -1.144781   China
    325   NASDAQ:DSWL   DSWL           -1.185771   China
    158     NYSE:ATHM   ATHM           -1.232777   China
    295   NASDAQ:FANH   FANH           -1.290323   China
    41      OTC:PINXY  PINXY           -1.379945   China
    255    NASDAQ:NIU    NIU           -1.408451   China
    40    NASDAQ:TCOM   TCOM           -1.426102   China
    45      OTC:BAIDF  BAIDF           -1.449275   China
    309     NYSE:BEDU   BEDU           -1.456311   China
    357     NASDAQ:YQ     YQ           -1.473297   China
    337   NASDAQ:EHGO   EHGO           -1.492537   China
    87      OTC:LGFRY  LGFRY           -1.590909   China
    363    NASDAQ:GMM    GMM           -1.628788   China
    278   NASDAQ:VIOT   VIOT           -1.675978   China
    371   NASDAQ:LOBO   LOBO           -1.686747   China
    358      OTC:IHGP   IHGP           -1.818182   China
    62      OTC:CCOZF  CCOZF           -1.858736   China
    305    NASDAQ:WOK    WOK           -1.875000   China
    429   NASDAQ:EZGO   EZGO           -2.119718   China
    244      NYSE:GHG    GHG           -2.173913   China
    411   NASDAQ:MLGO   MLGO           -2.354740   China
    139      NYSE:TAL    TAL           -2.376910   China
    423   NASDAQ:LXEH   LXEH           -2.459016   China
    90       NYSE:EDU    EDU           -2.509828   China
    424   NASDAQ:BTCT   BTCT           -2.580645   China
    331   NASDAQ:HUDI   HUDI           -2.602230   China
    266   NASDAQ:KNDI   KNDI           -2.631579   China
    388    NASDAQ:WTO    WTO           -2.636364   China
    367    NASDAQ:MMV    MMV           -2.746544   China
    437   NASDAQ:FRES   FRES           -2.777778   China
    445     NASDAQ:UK     UK           -2.857143   China
    166       NYSE:LU     LU           -2.891566   China
    396    NASDAQ:EJH    EJH           -2.912621   China
    140       NYSE:ZK     ZK           -2.922443   China
    438   NASDAQ:CNEY   CNEY           -3.015810   China
    332    NASDAQ:BGM    BGM           -3.080873   China
    239   NASDAQ:ZJYL   ZJYL           -3.088803   China
    385   NASDAQ:DTSS   DTSS           -3.151887   China
    65       NYSE:TME    TME           -3.160920   China
    376    NASDAQ:HLP    HLP           -3.220811   China
    444   NASDAQ:CLEU   CLEU           -3.225806   China
    9       OTC:PCCYF  PCCYF           -3.370787   China
    397   NASDAQ:AEHL   AEHL           -3.499028   China
    296   NASDAQ:PTHL   PTHL           -3.500000   China
    383    NASDAQ:JYD    JYD           -3.503733   China
    282   NASDAQ:TCJH   TCJH           -3.560606   China
    274   NASDAQ:THCH   THCH           -3.614458   China
    378     NASDAQ:PT     PT           -3.645833   China
    259     NASDAQ:EM     EM           -3.687500   China
    236    NASDAQ:YXT    YXT           -3.700000   China
    393   NASDAQ:NXTT   NXTT           -3.703704   China
    356     NASDAQ:JZ     JZ           -3.723887   China
    334      NYSE:CGA    CGA           -3.750000   China
    125     OTC:GNENY  GNENY           -4.056437   China
    257    NASDAQ:ANL    ANL           -4.081633   China
    414   NASDAQ:PAVS   PAVS           -4.166667   China
    360   NASDAQ:SEED   SEED           -4.334365   China
    400      OTC:PNYG   PNYG           -4.411765   China
    398   NASDAQ:RAYA   RAYA           -4.432432   China
    206     OTC:CASBF  CASBF           -4.451039   China
    202     NASDAQ:KC     KC           -4.645477   China
    291      NYSE:STG    STG           -4.696133   China
    262   NASDAQ:TOUR   TOUR           -4.729730   China
    381   NASDAQ:CJJD   CJJD           -4.830918   China
    408   NASDAQ:SNTG   SNTG           -4.862579   China
    51      OTC:CICOY  CICOY           -4.938272   China
    422     AMEX:CPHI   CPHI           -5.361217   China
    290   NASDAQ:ADAG   ADAG           -5.555556   China
    47      OTC:NNFSF  NNFSF           -5.686546   China
    201    NASDAQ:SDA    SDA           -5.755396   China
    294   NASDAQ:LGCL   LGCL           -5.882353   China
    133     OTC:SNPTF  SNPTF           -5.888298   China
    406      OTC:YBGJ   YBGJ           -5.982906   China
    273      NYSE:CNF    CNF           -6.132075   China
    432   NASDAQ:FAMI   FAMI           -6.143345   China
    431     OTC:LEJUY  LEJUY           -6.382979   China
    217      NYSE:YRD    YRD           -6.641604   China
    251    NASDAQ:ICG    ICG           -6.852248   China
    416   NASDAQ:CPOP   CPOP           -6.923077   China
    428   NASDAQ:JWEL   JWEL           -7.065217   China
    343   NASDAQ:AACG   AACG           -7.065217   China
    299   NASDAQ:CNTB   CNTB           -7.236842   China
    38      OTC:CIIHY  CIIHY           -7.676075   China
    275   NASDAQ:YIBO   YIBO           -8.256881   China
    348     NYSE:KUKE   KUKE           -8.271605   China
    377   NASDAQ:JZXN   JZXN           -8.280255   China
    289   NASDAQ:HOLO   HOLO           -8.514560   China
    440   NASDAQ:TANH   TANH           -8.524904   China
    387   NASDAQ:AIHS   AIHS           -8.695652   China
    375   NASDAQ:TCTM   TCTM           -8.917197   China
    281     OTC:CREQF  CREQF           -9.090909   China
    181      NYSE:RLX    RLX           -9.278351   China
    372   NASDAQ:UBXG   UBXG           -9.716418   China
    115     OTC:SHPMY  SHPMY          -10.087678   China
    237   NASDAQ:JFIN   JFIN          -10.352941   China
    407   NASDAQ:YGMZ   YGMZ          -10.778961   China
    231    NASDAQ:API    API          -11.132075   China
    80      OTC:CHVKF  CHVKF          -12.337662   China
    252    NASDAQ:HPH    HPH          -12.509259   China
    395   NASDAQ:GSUN   GSUN          -12.549801   China
    129     OTC:HPIFY  HPIFY          -12.679956   China
    340   NASDAQ:BDMD   BDMD          -13.253012   China
    443    NASDAQ:XHG    XHG          -13.333333   China
    312    NASDAQ:CCG    CCG          -14.759686   China
    450      OTC:KJFI   KJFI          -17.791411   China
    370   NASDAQ:KXIN   KXIN          -18.089142   China
    453      OTC:KAST   KAST          -20.000000   China
    134     OTC:SFOSF  SFOSF          -21.171171   China
    349      NYSE:XIN    XIN          -24.319419   China
    78      OTC:CHWRF  CHWRF          -26.923077   China
    439      OTC:SCAL   SCAL          -29.056604   China
    27     NASDAQ:DUO    DUO          -34.455959   China
    446     OTC:JPPYY  JPPYY          -50.247934   China
    178     OTC:CTRYF  CTRYF          -52.380952   China
    
    Total number of Chinese stocks: 477



```python
# Print available columns and data shape
print("Available columns:")
print(df.columns.tolist())
```

    Available columns:
    ['Symbol', 'Name', 'Description', 'All Time High', 'All Time Low', 'All Time Performance', 'Aroon Down (14)', 'Aroon Up (14)', 'Average Day Range (14)', 'Average Directional Index (14)', 'Average True Range (14)', 'Average Volume (10 day)', 'Average Volume (30 day)', 'Average Volume (60 day)', 'Average Volume (90 day)', 'Awesome Oscillator', 'Basic EPS (FY)', 'Basic EPS (TTM)', 'Bollinger Lower Band (20)', 'Bollinger Upper Band (20)', 'Bull Bear Power', 'Candle.3BlackCrows', 'Candle.3WhiteSoldiers', 'Candle.AbandonedBaby.Bearish', 'Candle.AbandonedBaby.Bullish', 'Candle.Doji', 'Candle.Doji.Dragonfly', 'Candle.Doji.Gravestone', 'Candle.Engulfing.Bearish', 'Candle.Engulfing.Bullish', 'Candle.EveningStar', 'Candle.Hammer', 'Candle.HangingMan', 'Candle.Harami.Bearish', 'Candle.Harami.Bullish', 'Candle.InvertedHammer', 'Candle.Kicking.Bearish', 'Candle.Kicking.Bullish', 'Candle.LongShadow.Lower', 'Candle.LongShadow.Upper', 'Candle.Marubozu.Black', 'Candle.Marubozu.White', 'Candle.MorningStar', 'Candle.ShootingStar', 'Candle.SpinningTop.Black', 'Candle.SpinningTop.White', 'Candle.TriStar.Bearish', 'Candle.TriStar.Bullish', 'Cash & Equivalents (FY)', 'Cash & Equivalents (MRQ)', 'Cash and short term investments (FY)', 'Cash and short term investments (MRQ)', 'Chaikin Money Flow (20)', 'Change', 'Change 15m', 'Change 15m, %', 'Change 1h', 'Change 1h, %', 'Change 1m', 'Change 1M', 'Change 1m, %', 'Change 1M, %', 'Change 1W', 'Change 1W, %', 'Change 4h', 'Change 4h, %', 'Change 5m', 'Change 5m, %', 'Change from Open', 'Change from Open %', 'Change %', 'Commodity Channel Index (20)', 'Country', 'Currency', 'Current Ratio (MRQ)', 'Debt to Equity Ratio (MRQ)', 'Dividends Paid (FY)', 'Dividends per share (Annual YoY Growth)', 'Dividends per Share (FY)', 'Dividends per Share (MRQ)', 'Dividend Yield Forward', 'Donchian Channels Lower Band (20)', 'Donchian Channels Upper Band (20)', 'EBITDA (Annual YoY Growth)', 'EBITDA (Quarterly QoQ Growth)', 'EBITDA (Quarterly YoY Growth)', 'EBITDA (TTM)', 'EBITDA (TTM YoY Growth)', 'Enterprise Value/EBITDA (TTM)', 'Enterprise Value (MRQ)', 'EPS Diluted (Annual YoY Growth)', 'EPS Diluted (FY)', 'EPS Diluted (MRQ)', 'EPS Diluted (Quarterly QoQ Growth)', 'EPS Diluted (Quarterly YoY Growth)', 'EPS Diluted (TTM)', 'EPS Diluted (TTM YoY Growth)', 'EPS Forecast (MRQ)', 'Exchange', 'Exponential Moving Average (10)', 'Exponential Moving Average (100)', 'Exponential Moving Average (20)', 'Exponential Moving Average (200)', 'Exponential Moving Average (30)', 'Exponential Moving Average (5)', 'Exponential Moving Average (50)', 'Free Cash Flow (Annual YoY Growth)', 'Free Cash Flow Margin (FY)', 'Free Cash Flow Margin (TTM)', 'Free Cash Flow (Quarterly QoQ Growth)', 'Free Cash Flow (Quarterly YoY Growth)', 'Free Cash Flow (TTM YoY Growth)', 'Fundamental Currency Code', 'Gap %', 'Goodwill', 'Gross Margin (FY)', 'Gross Margin (TTM)', 'Gross Profit (Annual YoY Growth)', 'Gross Profit (FY)', 'Gross Profit (MRQ)', 'Gross Profit (Quarterly QoQ Growth)', 'Gross Profit (Quarterly YoY Growth)', 'Gross Profit (TTM YoY Growth)', 'High', 'Hull Moving Average (9)', 'Ichimoku Base Line (9, 26, 52, 26)', 'Ichimoku Conversion Line (9, 26, 52, 26)', 'Ichimoku Leading Span A (9, 26, 52, 26)', 'Ichimoku Leading Span B (9, 26, 52, 26)', 'Industry', 'Keltner Channels Lower Band (20)', 'Keltner Channels Upper Band (20)', 'Last Year Revenue (FY)', 'Logoid', 'Low', 'MACD Level (12, 26)', 'MACD Signal (12, 26)', 'Market Capitalization', 'Momentum (10)', 'Money Flow (14)', 'Monthly Performance', '1-Month High', '3-Month High', '6-Month High', '1-Month Low', '3-Month Low', '6-Month Low', '3-Month Performance', '6-Month Performance', 'Moving Averages Rating', 'Negative Directional Indicator (14)', 'Net Debt (MRQ)', 'Net Income (Annual YoY Growth)', 'Net Income (FY)', 'Net Income (Quarterly QoQ Growth)', 'Net Income (Quarterly YoY Growth)', 'Net Income (TTM YoY Growth)', 'Net Margin (FY)', 'Net Margin (TTM)', 'Number of Employees', 'Number of Shareholders', 'Open', 'Operating Margin (FY)', 'Operating Margin (TTM)', 'Oscillators Rating', 'Parabolic SAR', 'Pivot Camarilla P', 'Pivot Camarilla R1', 'Pivot Camarilla R2', 'Pivot Camarilla R3', 'Pivot Camarilla S1', 'Pivot Camarilla S2', 'Pivot Camarilla S3', 'Pivot Classic P', 'Pivot Classic R1', 'Pivot Classic R2', 'Pivot Classic R3', 'Pivot Classic S1', 'Pivot Classic S2', 'Pivot Classic S3', 'Pivot DM P', 'Pivot DM R1', 'Pivot DM S1', 'Pivot Fibonacci P', 'Pivot Fibonacci R1', 'Pivot Fibonacci R2', 'Pivot Fibonacci R3', 'Pivot Fibonacci S1', 'Pivot Fibonacci S2', 'Pivot Fibonacci S3', 'Pivot Woodie P', 'Pivot Woodie R1', 'Pivot Woodie R2', 'Pivot Woodie R3', 'Pivot Woodie S1', 'Pivot Woodie S2', 'Pivot Woodie S3', 'Positive Directional Indicator (14)', 'Post-market Change', 'Post-market Change %', 'Post-market Close', 'Post-market High', 'Post-market Low', 'Post-market Open', 'Post-market Volume', 'Pre-market Change', 'Pre-market Change from Open', 'Pre-market Change from Open %', 'Pre-market Change %', 'Pre-market Close', 'Pre-market Gap %', 'Pre-market High', 'Pre-market Low', 'Pre-market Open', 'Pre-market Volume', 'Pretax Margin (TTM)', 'Price', 'Price to Book (FY)', 'Price to Book (MRQ)', 'Price to Earnings Ratio (TTM)', 'Price to Free Cash Flow (TTM)', 'Price to Revenue Ratio (TTM)', 'Price to Sales (FY)', 'Quick Ratio (MRQ)', 'Rate Of Change (9)', 'Recent Earnings Date', 'Relative Strength Index (14)', 'Relative Strength Index (7)', 'Relative Volume', 'Relative Volume at Time', 'Research & development Ratio (FY)', 'Research & development Ratio (TTM)', 'Return on Assets (TTM)', 'Return on Equity (TTM)', 'Return on Invested Capital (TTM)', 'Revenue (Annual YoY Growth)', 'Revenue per Employee (FY)', 'Revenue (Quarterly QoQ Growth)', 'Revenue (Quarterly YoY Growth)', 'Revenue (TTM YoY Growth)', 'Sector', 'Selling General & Admin expenses Ratio (FY)', 'Selling General & Admin expenses Ratio (TTM)', 'Shares Float', 'Simple Moving Average (10)', 'Simple Moving Average (100)', 'Simple Moving Average (20)', 'Simple Moving Average (200)', 'Simple Moving Average (30)', 'Simple Moving Average (5)', 'Simple Moving Average (50)', 'Stochastic %D (14, 3, 3)', 'Stochastic %K (14, 3, 3)', 'Stochastic RSI Fast (3, 3, 14, 14)', 'Stochastic RSI Slow (3, 3, 14, 14)', 'Submarket', 'Subtype', 'Technical Rating', 'Total Assets (Annual YoY Growth)', 'Total Assets (MRQ)', 'Total Assets (Quarterly QoQ Growth)', 'Total Assets (Quarterly YoY Growth)', 'Total Current Assets (MRQ)', 'Total Debt (Annual YoY Growth)', 'Total Debt (MRQ)', 'Total Debt (Quarterly QoQ Growth)', 'Total Debt (Quarterly YoY Growth)', 'Total Liabilities (FY)', 'Total Liabilities (MRQ)', 'Total Revenue (FY)', 'Total Shares Outstanding', 'Type', 'Ultimate Oscillator (7, 14, 28)', 'Upcoming Earnings Date', 'Volatility', 'Volatility Month', 'Volatility Week', 'Volume', 'Volume*Price', 'Volume Weighted Average Price', 'Volume Weighted Moving Average (20)', 'Weekly Performance', '52 Week High', '52 Week Low', 'Williams Percent Range (14)', 'Yearly Performance', '1-Year Beta', 'YTD Performance', '5Y Performance', 'Reco. BBPower', 'Reco. HullMA9', 'Reco. UO', 'Reco. VWMA', 'Prev. Awesome Oscillator', 'Prev. Commodity Channel Index (20)', 'Prev. Momentum (10)', 'Prev. Negative Directional Indicator (14)', 'Prev. Positive Directional Indicator (14)', 'Prev. Relative Strength Index (14)', 'Prev. Relative Strength Index (7)', 'Prev. Stochastic %D (14, 3, 3)', 'Prev. Stochastic %K (14, 3, 3)']



```python

```
