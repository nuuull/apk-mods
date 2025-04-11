package com.cmplay.dancingline;

import android.app.Activity;
import android.content.Context;
import android.content.SharedPreferences;

public class Hack {

    private static final String[] levels = {
            "Intro",
            "Seasons",
            "Storm",
            "Desert",
            "Chaos",
            "Autumn",
            "ComingSoon",
            "Piano",
            "Plains",
            "Crystal",
            "Cathedral",
            "Morning",
            "EarthDay",
            "WinterHouseRemix",
            "PianoRemix",
            "Mountains",
            "China",
            "Pirates",
            "PlainsRemix",
            "Faded",
            "Beginning",
            "Haloween",
            "AllAboutUs",
            "Maze",
            "Africa",
            "ChristmasEve",
            "Valentines",
            "StormRemix",
            "West",
            "Faded8bit",
            "Spring",
            "Heaven",
            "HipHop",
            "Football",
            "Duck",
            "Fantasy",
            "Despacito",
            "HalloweenRemix",
            "Alone",
            "Race",
            "EarthDayRemix",
            "Christmas",
            "TheEnd",
            "SpringFestival",
            "Ocean",
            "SpringAwake",
            "Alley",
            "Comegetit",
            "Heaven_color",
            "ScoreMode",
            "EpicCathedral",
            "Easter",
            "Taurus",
            "PlayerGudie",
            "TheExodus",
            "Basketball",
            "TheWar",
            "Park",
            "LoveStory",
            "ThirdAnniversary",
            "VideoGame",
            "Samurai",
            "Tutorial",
            "TheJournay",
            "TheWizardOfOz",
            "Dragon"
    };

    private static final String[] skins = {
            "Line",
            "Cap",
            "CowBoy",
            "Headphones",
            "Particle2",
            "Particle3",
            "Mascot",
            "Rainbow",
            "Module",
            "Lightining",
            "Stalagmite",
            "RockLine",
            "ChineseDragon",
            "Chaos",
            "Mountains",
            "Jelly",
            "Snowball",
            "PaintBrush",
            "Balloon",
            "Cloud",
            "Light",
            "TombStone",
            "Frankenstein",
            "Witch",
            "Snake",
            "Slither",
            "Arrow",
            "Robot",
            "Football",
            "Domino",
            "Jester",
            "Mage",
            "Skeleton"
    };

    public static void unlock(Context context) {
        SharedPreferences prefs = context.getSharedPreferences("com.cmplay.dancingline.v2.playerprefs", Activity.MODE_PRIVATE);
        SharedPreferences.Editor settings = prefs.edit();

        settings.putInt("subscribe_key_time", Integer.MAX_VALUE);
        settings.putInt("subscribe_key_number", 2);
        settings.putInt("AreAdsBlockedNew", 1);

        if (prefs.getInt("mod_patch_version", 0) != 1) {
            settings.putString("Decorate_HatType_Unlock", "1-2-3-4-5-5-4-3-2-1");
            settings.putString("infinityHeartModeTimeEnd", "2500,4,15,20,49,30");
            settings.putString("infinityModeTimeEnd", "2500,4,15,20,49,30");

            for (String level : levels) {
                settings.putInt("levelUnlockDataName_".concat(level), 1);
            }

            for (String skin : skins) {
                settings.putInt("UnlockedSettingsDataKey_".concat(skin), 1);
            }

            settings.putInt("mod_patch_version", 1);
        }

        settings.apply();
    }
}
