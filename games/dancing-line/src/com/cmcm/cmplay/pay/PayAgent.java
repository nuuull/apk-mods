package com.cmcm.cmplay.pay;

import android.app.Activity;
import android.content.Intent;

/* loaded from: classes.dex */
public abstract class PayAgent {

    public abstract void onCreate(Activity activity);

    public abstract void onDestroy(Activity activity);

    public abstract void onNewIntent(Intent intent);

    public abstract void onPause(Activity activity);

    public abstract void onRestart(Activity activity);

    public abstract void onResume(Activity activity);

    public abstract void onStart(Activity activity);

    public abstract void onStop(Activity activity);

    public abstract void pay(String str, String str2, PayCallBack payCallBack);

    protected void setProductInfoGenerator(AbsProductInfoGenerator absProductInfoGenerator) {
    }

    public AbsProductInfoGenerator getProductInfoGenerator() {
        return null;
    }

    public void setPayCallBack(PayCallBack payCallBack) {
    }

    public PayCallBack getPayCallBack() {
        return null;
    }
}
