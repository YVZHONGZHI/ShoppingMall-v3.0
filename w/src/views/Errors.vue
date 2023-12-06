<template>
    <div class="errors">
        <p><b>404.</b>抱歉, 您访问的资源不存在.</p>
        <p class="d">请确认您输入的网址是否正确, 如果问题持续存在, 请发邮件至 YVZHONGZHI@qq.com 与我们联系.</p>
        <p><a href="" @click="goPage('/home')">返回网站首页</a></p>
    </div>
</template>


<script>
    export default {
        name: "Errors",
        methods: {
            goPage(url_path) {
                this.$router.push(url_path)
            }
        }
    }
</script>


<style scoped>
    .errors {
        padding: 10px;
        font-size: 14px;
        max-width: 550px;
        min-height: 200px;
        margin: 8% auto 0;
    }

    p {
        color: #555;
        margin: 10px 10px;
    }
</style>