import re
import sys
from pathlib import Path

BASE_REMOVE_METHODS = (
    "initAd",
    "onActivityResult",
    "onDestroy",
    "onPause",
    "onRestart",
    "onResume",
    "onStart",
    "onStop"
)

MANIFEST_REMOVE_PERMISSIONS = (
    "android.permission.READ_EXTERNAL_STORAGE",
    "android.permission.CHANGE_WIFI_STATE",
    "android.permission.REQUEST_INSTALL_PACKAGES",
    "android.permission.ACCESS_FINE_LOCATION",
    "android.permission.QUERY_ALL_PACKAGES",
    "android.permission.CHANGE_NETWORK_STATE"
)

HACK_SMALI = r"""
.class public Lcom/cmplay/dancingline/Hack;
.super Ljava/lang/Object;
.source "Hack.java"


# static fields
.field private static final levels:[Ljava/lang/String;

.field private static final skins:[Ljava/lang/String;


# direct methods
.method static constructor <clinit>()V
    .registers 8

    .prologue
    const/4 v7, 0x4

    const/4 v6, 0x3

    const/4 v5, 0x2

    const/4 v4, 0x1

    const/4 v3, 0x0

    .line 9
    const/16 v0, 0x42

    new-array v0, v0, [Ljava/lang/String;

    const-string v1, "Intro"

    aput-object v1, v0, v3

    const-string v1, "Seasons"

    aput-object v1, v0, v4

    const-string v1, "Storm"

    aput-object v1, v0, v5

    const-string v1, "Desert"

    aput-object v1, v0, v6

    const-string v1, "Chaos"

    aput-object v1, v0, v7

    const/4 v1, 0x5

    const-string v2, "Autumn"

    aput-object v2, v0, v1

    const/4 v1, 0x6

    const-string v2, "ComingSoon"

    aput-object v2, v0, v1

    const/4 v1, 0x7

    const-string v2, "Piano"

    aput-object v2, v0, v1

    const/16 v1, 0x8

    const-string v2, "Plains"

    aput-object v2, v0, v1

    const/16 v1, 0x9

    const-string v2, "Crystal"

    aput-object v2, v0, v1

    const/16 v1, 0xa

    const-string v2, "Cathedral"

    aput-object v2, v0, v1

    const/16 v1, 0xb

    const-string v2, "Morning"

    aput-object v2, v0, v1

    const/16 v1, 0xc

    const-string v2, "EarthDay"

    aput-object v2, v0, v1

    const/16 v1, 0xd

    const-string v2, "WinterHouseRemix"

    aput-object v2, v0, v1

    const/16 v1, 0xe

    const-string v2, "PianoRemix"

    aput-object v2, v0, v1

    const/16 v1, 0xf

    const-string v2, "Mountains"

    aput-object v2, v0, v1

    const/16 v1, 0x10

    const-string v2, "China"

    aput-object v2, v0, v1

    const/16 v1, 0x11

    const-string v2, "Pirates"

    aput-object v2, v0, v1

    const/16 v1, 0x12

    const-string v2, "PlainsRemix"

    aput-object v2, v0, v1

    const/16 v1, 0x13

    const-string v2, "Faded"

    aput-object v2, v0, v1

    const/16 v1, 0x14

    const-string v2, "Beginning"

    aput-object v2, v0, v1

    const/16 v1, 0x15

    const-string v2, "Haloween"

    aput-object v2, v0, v1

    const/16 v1, 0x16

    const-string v2, "AllAboutUs"

    aput-object v2, v0, v1

    const/16 v1, 0x17

    const-string v2, "Maze"

    aput-object v2, v0, v1

    const/16 v1, 0x18

    const-string v2, "Africa"

    aput-object v2, v0, v1

    const/16 v1, 0x19

    const-string v2, "ChristmasEve"

    aput-object v2, v0, v1

    const/16 v1, 0x1a

    const-string v2, "Valentines"

    aput-object v2, v0, v1

    const/16 v1, 0x1b

    const-string v2, "StormRemix"

    aput-object v2, v0, v1

    const/16 v1, 0x1c

    const-string v2, "West"

    aput-object v2, v0, v1

    const/16 v1, 0x1d

    const-string v2, "Faded8bit"

    aput-object v2, v0, v1

    const/16 v1, 0x1e

    const-string v2, "Spring"

    aput-object v2, v0, v1

    const/16 v1, 0x1f

    const-string v2, "Heaven"

    aput-object v2, v0, v1

    const/16 v1, 0x20

    const-string v2, "HipHop"

    aput-object v2, v0, v1

    const/16 v1, 0x21

    const-string v2, "Football"

    aput-object v2, v0, v1

    const/16 v1, 0x22

    const-string v2, "Duck"

    aput-object v2, v0, v1

    const/16 v1, 0x23

    const-string v2, "Fantasy"

    aput-object v2, v0, v1

    const/16 v1, 0x24

    const-string v2, "Despacito"

    aput-object v2, v0, v1

    const/16 v1, 0x25

    const-string v2, "HalloweenRemix"

    aput-object v2, v0, v1

    const/16 v1, 0x26

    const-string v2, "Alone"

    aput-object v2, v0, v1

    const/16 v1, 0x27

    const-string v2, "Race"

    aput-object v2, v0, v1

    const/16 v1, 0x28

    const-string v2, "EarthDayRemix"

    aput-object v2, v0, v1

    const/16 v1, 0x29

    const-string v2, "Christmas"

    aput-object v2, v0, v1

    const/16 v1, 0x2a

    const-string v2, "TheEnd"

    aput-object v2, v0, v1

    const/16 v1, 0x2b

    const-string v2, "SpringFestival"

    aput-object v2, v0, v1

    const/16 v1, 0x2c

    const-string v2, "Ocean"

    aput-object v2, v0, v1

    const/16 v1, 0x2d

    const-string v2, "SpringAwake"

    aput-object v2, v0, v1

    const/16 v1, 0x2e

    const-string v2, "Alley"

    aput-object v2, v0, v1

    const/16 v1, 0x2f

    const-string v2, "Comegetit"

    aput-object v2, v0, v1

    const/16 v1, 0x30

    const-string v2, "Heaven_color"

    aput-object v2, v0, v1

    const/16 v1, 0x31

    const-string v2, "ScoreMode"

    aput-object v2, v0, v1

    const/16 v1, 0x32

    const-string v2, "EpicCathedral"

    aput-object v2, v0, v1

    const/16 v1, 0x33

    const-string v2, "Easter"

    aput-object v2, v0, v1

    const/16 v1, 0x34

    const-string v2, "Taurus"

    aput-object v2, v0, v1

    const/16 v1, 0x35

    const-string v2, "PlayerGudie"

    aput-object v2, v0, v1

    const/16 v1, 0x36

    const-string v2, "TheExodus"

    aput-object v2, v0, v1

    const/16 v1, 0x37

    const-string v2, "Basketball"

    aput-object v2, v0, v1

    const/16 v1, 0x38

    const-string v2, "TheWar"

    aput-object v2, v0, v1

    const/16 v1, 0x39

    const-string v2, "Park"

    aput-object v2, v0, v1

    const/16 v1, 0x3a

    const-string v2, "LoveStory"

    aput-object v2, v0, v1

    const/16 v1, 0x3b

    const-string v2, "ThirdAnniversary"

    aput-object v2, v0, v1

    const/16 v1, 0x3c

    const-string v2, "VideoGame"

    aput-object v2, v0, v1

    const/16 v1, 0x3d

    const-string v2, "Samurai"

    aput-object v2, v0, v1

    const/16 v1, 0x3e

    const-string v2, "Tutorial"

    aput-object v2, v0, v1

    const/16 v1, 0x3f

    const-string v2, "TheJournay"

    aput-object v2, v0, v1

    const/16 v1, 0x40

    const-string v2, "TheWizardOfOz"

    aput-object v2, v0, v1

    const/16 v1, 0x41

    const-string v2, "Dragon"

    aput-object v2, v0, v1

    sput-object v0, Lcom/cmplay/dancingline/Hack;->levels:[Ljava/lang/String;

    .line 78
    const/16 v0, 0x21

    new-array v0, v0, [Ljava/lang/String;

    const-string v1, "Line"

    aput-object v1, v0, v3

    const-string v1, "Cap"

    aput-object v1, v0, v4

    const-string v1, "CowBoy"

    aput-object v1, v0, v5

    const-string v1, "Headphones"

    aput-object v1, v0, v6

    const-string v1, "Particle2"

    aput-object v1, v0, v7

    const/4 v1, 0x5

    const-string v2, "Particle3"

    aput-object v2, v0, v1

    const/4 v1, 0x6

    const-string v2, "Mascot"

    aput-object v2, v0, v1

    const/4 v1, 0x7

    const-string v2, "Rainbow"

    aput-object v2, v0, v1

    const/16 v1, 0x8

    const-string v2, "Module"

    aput-object v2, v0, v1

    const/16 v1, 0x9

    const-string v2, "Lightining"

    aput-object v2, v0, v1

    const/16 v1, 0xa

    const-string v2, "Stalagmite"

    aput-object v2, v0, v1

    const/16 v1, 0xb

    const-string v2, "RockLine"

    aput-object v2, v0, v1

    const/16 v1, 0xc

    const-string v2, "ChineseDragon"

    aput-object v2, v0, v1

    const/16 v1, 0xd

    const-string v2, "Chaos"

    aput-object v2, v0, v1

    const/16 v1, 0xe

    const-string v2, "Mountains"

    aput-object v2, v0, v1

    const/16 v1, 0xf

    const-string v2, "Jelly"

    aput-object v2, v0, v1

    const/16 v1, 0x10

    const-string v2, "Snowball"

    aput-object v2, v0, v1

    const/16 v1, 0x11

    const-string v2, "PaintBrush"

    aput-object v2, v0, v1

    const/16 v1, 0x12

    const-string v2, "Balloon"

    aput-object v2, v0, v1

    const/16 v1, 0x13

    const-string v2, "Cloud"

    aput-object v2, v0, v1

    const/16 v1, 0x14

    const-string v2, "Light"

    aput-object v2, v0, v1

    const/16 v1, 0x15

    const-string v2, "TombStone"

    aput-object v2, v0, v1

    const/16 v1, 0x16

    const-string v2, "Frankenstein"

    aput-object v2, v0, v1

    const/16 v1, 0x17

    const-string v2, "Witch"

    aput-object v2, v0, v1

    const/16 v1, 0x18

    const-string v2, "Snake"

    aput-object v2, v0, v1

    const/16 v1, 0x19

    const-string v2, "Slither"

    aput-object v2, v0, v1

    const/16 v1, 0x1a

    const-string v2, "Arrow"

    aput-object v2, v0, v1

    const/16 v1, 0x1b

    const-string v2, "Robot"

    aput-object v2, v0, v1

    const/16 v1, 0x1c

    const-string v2, "Football"

    aput-object v2, v0, v1

    const/16 v1, 0x1d

    const-string v2, "Domino"

    aput-object v2, v0, v1

    const/16 v1, 0x1e

    const-string v2, "Jester"

    aput-object v2, v0, v1

    const/16 v1, 0x1f

    const-string v2, "Mage"

    aput-object v2, v0, v1

    const/16 v1, 0x20

    const-string v2, "Skeleton"

    aput-object v2, v0, v1

    sput-object v0, Lcom/cmplay/dancingline/Hack;->skins:[Ljava/lang/String;

    return-void
.end method

.method public constructor <init>()V
    .registers 1

    .prologue
    .line 7
    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method public static unlock(Landroid/content/Context;)V
    .registers 9

    .prologue
    const/4 v0, 0x0

    const/4 v7, 0x1

    .line 115
    const-string v1, "com.cmplay.dancingline.v2.playerprefs"

    invoke-virtual {p0, v1, v0}, Landroid/content/Context;->getSharedPreferences(Ljava/lang/String;I)Landroid/content/SharedPreferences;

    move-result-object v1

    .line 116
    invoke-interface {v1}, Landroid/content/SharedPreferences;->edit()Landroid/content/SharedPreferences$Editor;

    move-result-object v2

    .line 118
    const-string v3, "subscribe_key_time"

    const v4, 0x7fffffff

    invoke-interface {v2, v3, v4}, Landroid/content/SharedPreferences$Editor;->putInt(Ljava/lang/String;I)Landroid/content/SharedPreferences$Editor;

    .line 119
    const-string v3, "subscribe_key_number"

    const/4 v4, 0x2

    invoke-interface {v2, v3, v4}, Landroid/content/SharedPreferences$Editor;->putInt(Ljava/lang/String;I)Landroid/content/SharedPreferences$Editor;

    .line 120
    const-string v3, "AreAdsBlockedNew"

    invoke-interface {v2, v3, v7}, Landroid/content/SharedPreferences$Editor;->putInt(Ljava/lang/String;I)Landroid/content/SharedPreferences$Editor;

    .line 122
    const-string v3, "mod_patch_version"

    invoke-interface {v1, v3, v0}, Landroid/content/SharedPreferences;->getInt(Ljava/lang/String;I)I

    move-result v1

    if-eq v1, v7, :cond_68

    .line 123
    const-string v1, "Decorate_HatType_Unlock"

    const-string v3, "1-2-3-4-5-5-4-3-2-1"

    invoke-interface {v2, v1, v3}, Landroid/content/SharedPreferences$Editor;->putString(Ljava/lang/String;Ljava/lang/String;)Landroid/content/SharedPreferences$Editor;

    .line 124
    const-string v1, "infinityHeartModeTimeEnd"

    const-string v3, "2500,4,15,20,49,30"

    invoke-interface {v2, v1, v3}, Landroid/content/SharedPreferences$Editor;->putString(Ljava/lang/String;Ljava/lang/String;)Landroid/content/SharedPreferences$Editor;

    .line 125
    const-string v1, "infinityModeTimeEnd"

    const-string v3, "2500,4,15,20,49,30"

    invoke-interface {v2, v1, v3}, Landroid/content/SharedPreferences$Editor;->putString(Ljava/lang/String;Ljava/lang/String;)Landroid/content/SharedPreferences$Editor;

    .line 127
    sget-object v3, Lcom/cmplay/dancingline/Hack;->levels:[Ljava/lang/String;

    array-length v4, v3

    move v1, v0

    :goto_40
    if-ge v1, v4, :cond_50

    aget-object v5, v3, v1

    .line 128
    const-string v6, "levelUnlockDataName_"

    invoke-virtual {v6, v5}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v5

    invoke-interface {v2, v5, v7}, Landroid/content/SharedPreferences$Editor;->putInt(Ljava/lang/String;I)Landroid/content/SharedPreferences$Editor;

    .line 127
    add-int/lit8 v1, v1, 0x1

    goto :goto_40

    .line 131
    :cond_50
    sget-object v1, Lcom/cmplay/dancingline/Hack;->skins:[Ljava/lang/String;

    array-length v3, v1

    :goto_53
    if-ge v0, v3, :cond_63

    aget-object v4, v1, v0

    .line 132
    const-string v5, "UnlockedSettingsDataKey_"

    invoke-virtual {v5, v4}, Ljava/lang/String;->concat(Ljava/lang/String;)Ljava/lang/String;

    move-result-object v4

    invoke-interface {v2, v4, v7}, Landroid/content/SharedPreferences$Editor;->putInt(Ljava/lang/String;I)Landroid/content/SharedPreferences$Editor;

    .line 131
    add-int/lit8 v0, v0, 0x1

    goto :goto_53

    .line 135
    :cond_63
    const-string v0, "mod_patch_version"

    invoke-interface {v2, v0, v7}, Landroid/content/SharedPreferences$Editor;->putInt(Ljava/lang/String;I)Landroid/content/SharedPreferences$Editor;

    .line 138
    :cond_68
    invoke-interface {v2}, Landroid/content/SharedPreferences$Editor;->apply()V

    .line 139
    return-void
.end method
"""

TAPTAPPAY_SMALI = r"""
.class public Lcom/cmcm/cmplay/pay/TaptapPay;
.super Lcom/cmcm/cmplay/pay/PayAgent;
.source "TaptapPay.java"


# static fields
.field private static sInstance:Lcom/cmcm/cmplay/pay/TaptapPay;


# direct methods
.method private constructor <init>()V
    .registers 1

    .prologue
    .line 29
    invoke-direct {p0}, Lcom/cmcm/cmplay/pay/PayAgent;-><init>()V

    .line 30
    return-void
.end method

.method public static getInstance()Lcom/cmcm/cmplay/pay/TaptapPay;
    .registers 2

    .prologue
    .line 33
    sget-object v0, Lcom/cmcm/cmplay/pay/TaptapPay;->sInstance:Lcom/cmcm/cmplay/pay/TaptapPay;

    if-nez v0, :cond_13

    .line 34
    const-class v1, Lcom/cmcm/cmplay/pay/TaptapPay;

    monitor-enter v1

    .line 35
    :try_start_7
    sget-object v0, Lcom/cmcm/cmplay/pay/TaptapPay;->sInstance:Lcom/cmcm/cmplay/pay/TaptapPay;

    if-nez v0, :cond_12

    .line 36
    new-instance v0, Lcom/cmcm/cmplay/pay/TaptapPay;

    invoke-direct {v0}, Lcom/cmcm/cmplay/pay/TaptapPay;-><init>()V

    sput-object v0, Lcom/cmcm/cmplay/pay/TaptapPay;->sInstance:Lcom/cmcm/cmplay/pay/TaptapPay;

    .line 38
    :cond_12
    monitor-exit v1
    :try_end_13
    .catchall {:try_start_7 .. :try_end_13} :catchall_16

    .line 40
    :cond_13
    sget-object v0, Lcom/cmcm/cmplay/pay/TaptapPay;->sInstance:Lcom/cmcm/cmplay/pay/TaptapPay;

    return-object v0

    .line 38
    :catchall_16
    move-exception v0

    :try_start_17
    monitor-exit v1
    :try_end_18
    .catchall {:try_start_17 .. :try_end_18} :catchall_16

    throw v0
.end method


# virtual methods
.method public getUserId()Ljava/lang/String;
    .registers 2

    .prologue
    .line 67
    const-string v0, "WAAAHHHH"

    return-object v0
.end method

.method public onCreate(Landroid/app/Activity;)V
    .registers 4

    .prologue
    .line 53
    new-instance v0, Lcom/cmcm/cmplay/pay/ProductInfoGenerator;

    invoke-direct {v0}, Lcom/cmcm/cmplay/pay/ProductInfoGenerator;-><init>()V

    .line 54
    const/4 v1, 0x4

    invoke-virtual {v0, p1, v1}, Lcom/cmcm/cmplay/pay/ProductInfoGenerator;->init(Landroid/app/Activity;I)V

    .line 55
    invoke-virtual {p0, v0}, Lcom/cmcm/cmplay/pay/TaptapPay;->setProductInfoGenerator(Lcom/cmcm/cmplay/pay/AbsProductInfoGenerator;)V

    .line 56
    return-void
.end method

.method public onDestroy(Landroid/app/Activity;)V
    .registers 2

    .prologue
    .line 11
    return-void
.end method

.method public onNewIntent(Landroid/content/Intent;)V
    .registers 2

    .prologue
    .line 64
    return-void
.end method

.method public onPause(Landroid/app/Activity;)V
    .registers 2

    .prologue
    .line 15
    return-void
.end method

.method public onRestart(Landroid/app/Activity;)V
    .registers 2

    .prologue
    .line 19
    return-void
.end method

.method public onResume(Landroid/app/Activity;)V
    .registers 2

    .prologue
    .line 60
    return-void
.end method

.method public onStart(Landroid/app/Activity;)V
    .registers 2

    .prologue
    .line 23
    return-void
.end method

.method public onStop(Landroid/app/Activity;)V
    .registers 2

    .prologue
    .line 27
    return-void
.end method

.method public pay(Ljava/lang/String;Ljava/lang/String;Lcom/cmcm/cmplay/pay/PayCallBack;)V
    .registers 7

    .prologue
    .line 45
    invoke-virtual {p0, p3}, Lcom/cmcm/cmplay/pay/TaptapPay;->setPayCallBack(Lcom/cmcm/cmplay/pay/PayCallBack;)V

    .line 46
    invoke-virtual {p0}, Lcom/cmcm/cmplay/pay/TaptapPay;->getPayCallBack()Lcom/cmcm/cmplay/pay/PayCallBack;

    move-result-object v0

    if-eqz v0, :cond_14

    .line 47
    invoke-virtual {p0}, Lcom/cmcm/cmplay/pay/TaptapPay;->getPayCallBack()Lcom/cmcm/cmplay/pay/PayCallBack;

    move-result-object v0

    const-string v1, "000"

    const/16 v2, 0x10

    invoke-interface {v0, p1, p2, v1, v2}, Lcom/cmcm/cmplay/pay/PayCallBack;->onPayCallbackSucced(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;I)V

    .line 49
    :cond_14
    return-void
.end method
"""

ANTIADDICTION_SMALI = r"""
.class public Lcom/cmplay/dancingline/util/AntiAddictionKitUtil;
.super Ljava/lang/Object;
.source "AntiAddictionKitUtil.java"


# direct methods
.method public constructor <init>()V
    .registers 1

    .prologue
    .line 6
    invoke-direct {p0}, Ljava/lang/Object;-><init>()V

    return-void
.end method

.method public static getAndroidId(Landroid/content/Context;)Ljava/lang/String;
    .registers 2

    .prologue
    .line 13
    const-string v0, "00000"

    return-object v0
.end method

.method public static isBoolAntiAddiction()Z
    .registers 1

    .prologue
    .line 9
    const/4 v0, 0x0

    return v0
.end method
"""

def patch_source(source_path):

    if not Path(source_path).is_dir():
        print("Path is not a directory.", file=sys.stderr)
        exit(1)

    with open(f"{source_path}/smali/com/cmplay/dancingline/BaseAppActivity.smali", "r+") as file:
        data = re.sub(fr'.method (?:protected|public|private) (?:{'|'.join(BASE_REMOVE_METHODS)})(?s:.*?).end method|.line 49(?s:.*?)(?=return-void)', '', file.read())
        file.seek(0)
        file.write(data)
        file.truncate()

    with open(f"{source_path}/AndroidManifest.xml", "r+") as file:
        data = re.sub(r'<activity(?s:.*?)com.cmplay.permisson.NewLauncheActivity(?s:.*?)</activity>', '', file.read())
        data = re.sub(r'(com.cmplay.dancingline.BaseAppActivity(?s:.*?)>)', r'''\1
            <intent-filter>
                <action android:name="android.intent.action.MAIN"/>
                <category android:name="android.intent.category.LAUNCHER"/>
            </intent-filter>
            ''', data)
        data = re.sub(fr'<uses-permission.*?(?:{'|'.join(MANIFEST_REMOVE_PERMISSIONS)}).*>', '', data)
        file.seek(0)
        file.write(data)
        file.truncate()

    with open(f"{source_path}/res/values/strings.xml", "r+") as file:
        data = file.read()
        data = data.replace("跳舞的线", "Dancing Line")
        file.seek(0)
        file.write(data)
        file.truncate()

    with open(f"{source_path}/smali/com/cmplay/dancingline/GameApp.smali", "r+") as file:
        data = re.sub(r"(invoke-super {p0}, Lcom/cmcm/cmplay/BaseApplication;->onCreate\(\)V)", r"""\1

        invoke-static {p0}, Lcom/cmplay/dancingline/Hack;->unlock(Landroid/content/Context;)V
        """, file.read())
        file.seek(0)
        file.write(data)
        file.truncate()

    open(f"{source_path}/smali/com/cmplay/dancingline/Hack.smali", "w").write(HACK_SMALI)

    open(f"{source_path}/smali/com/cmcm/cmplay/pay/TaptapPay.smali", "w").write(TAPTAPPAY_SMALI)

    open(f"{source_path}/smali/com/cmplay/dancingline/util/AntiAddictionKitUtil.smali", "w").write(ANTIADDICTION_SMALI)

    print("Done!")

if __name__ == "__main__":
    patch_source(sys.argv[1])
