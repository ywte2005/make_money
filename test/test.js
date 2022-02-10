function goToPage() {
    toastLog("打开钉钉中...");
    launch("com.alibaba.android.rimet");
    waitStart();
    log("启动完成");
    loginIfNeed();
    sleep(waitTime * 1000);
    setLog("进入打卡页面");
    var a = app.intent({
        action: "VIEW",
        data: "dingtalk://dingtalkclient/page/link?url=https://attend.dingtalk.com/attend/index.html"
    });
    app.startActivity(a);
}

goToPage()