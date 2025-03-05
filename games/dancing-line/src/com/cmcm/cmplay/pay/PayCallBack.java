package com.cmcm.cmplay.pay;

public interface PayCallBack {
    public static final int PAY_FAILED = 200;
    public static final int PAY_FAILED_CANCEL = 204;
    public static final int PAY_FAILED_DATAERROR = 203;
    public static final int PAY_FAILED_HAS_REMAIN_ORDER = 205;
    public static final int PAY_FAILED_NETERROR = 201;
    public static final int PAY_FAILED_SEVERERROR = 202;
    public static final int PAY_SUCESSED = 100;

    void onPayCallbackFailed(int i);

    void onPayCallbackSucced(String str, String str2, String str3, int i);
}
