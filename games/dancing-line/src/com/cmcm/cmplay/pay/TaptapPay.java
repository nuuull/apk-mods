package com.cmcm.cmplay.pay;

import android.app.Activity;
import android.content.Intent;

public class TaptapPay extends PayAgent {
    private static TaptapPay sInstance;

    @Override
    public void onDestroy(Activity activity) {
    }

    @Override
    public void onPause(Activity activity) {
    }

    @Override
    public void onRestart(Activity activity) {
    }

    @Override
    public void onStart(Activity activity) {
    }

    @Override
    public void onStop(Activity activity) {
    }

    private TaptapPay() {
    }

    public static TaptapPay getInstance() {
        if (sInstance == null) {
            synchronized (TaptapPay.class) {
                if (sInstance == null) {
                    sInstance = new TaptapPay();
                }
            }
        }
        return sInstance;
    }

    @Override
    public void pay(String str, String str2, PayCallBack payCallBack) {
        setPayCallBack(payCallBack);
        if (getPayCallBack() != null) {
            getPayCallBack().onPayCallbackSucced(str, str2, "000", 16);
        }
    }

    @Override
    public void onCreate(Activity activity) {
        ProductInfoGenerator productInfoGenerator = new ProductInfoGenerator();
        productInfoGenerator.init(activity, 4);
        setProductInfoGenerator(productInfoGenerator);
    }

    @Override
    public void onResume(Activity activity) {
    }

    @Override
    public void onNewIntent(Intent intent) {
    }

    public String getUserId() {
        return "WAAAHHHH";
    }

}
