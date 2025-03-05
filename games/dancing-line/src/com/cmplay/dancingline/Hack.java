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
            "CowBoy",
            "Particle2",
            "Particle3",
            "Mascot",
            "Rainbow",
            "Module",
            "Stalagmite",
            "RockLine",
            "ChineseDragon",
            "Snowball",
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
            "Domino",
            "Jester",
            "Mage",
            "Skeleton",
    };

    public static void unlock(Context context) {
        SharedPreferences sharedPrefs = context.getSharedPreferences("com.cmplay.dancingline.v2.playerprefs",
                Activity.MODE_PRIVATE);
        SharedPreferences.Editor settings = sharedPrefs.edit();

        settings.putInt("subscribe_key_time", Integer.MAX_VALUE);
        settings.putInt("subscribe_key_number", 2);

        if (sharedPrefs.getBoolean("is_first_unlock", true)) {
            settings.putString("Decorate_HatType_Unlock", "1-2-3-4-5-5-4-3-2-1");
            settings.putString("infinityHeartModeTimeEnd", "2500,4,15,20,49,30");
            settings.putString("infinityModeTimeEnd", "2500,4,15,20,49,30");

            for (String level : levels) {
                settings.putInt("levelUnlockDataName_".concat(level), 1);
            }

            for (String skin : skins) {
                settings.putInt("UnlockedSettingsDataKey_".concat(skin), 1);
            }

            settings.putBoolean("is_first_unlock", false);
        }

        settings.apply();
    }
}
