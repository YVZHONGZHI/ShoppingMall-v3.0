<template>
    <div class="login">
        <div class="div1">
            <h1>中  文  用  户  登  录  页  面</h1>
            <div class="div2">
                <label for="w">
                    <img src="../assets/img/w.png" width="24" height="24" alt="用户名图标">
                    <input type="text" id="w" name="username" class="label1" placeholder="用 户 名" v-model="username">
                </label>
            </div>
            <div class="div2">
                <label for="p">
                    <img src="../assets/img/w1.png" width="24" height="24" alt="密码图标">
                    <input type="password" id="p" name="password" class="label1" placeholder="密 码" v-model="password">
                </label>
            </div>
            <input type="button" value="登    录" class="label2" @click="login">
        </div>
    </div>
</template>


<script>
    export default {
        name: "Login",
        data() {
            return {
                username: '',
                password: ''
            }
        },
        methods: {
            login() {
                if (this.username && this.password) {
                    this.$axios.post(this.$settings.base_url+'/login/', {
                        username: this.username,
                        password: this.password
                    }).then(response => {
                        if (response.data.code) {
                            this.$cookies.set('username', response.data.username, '7d')
                            this.$cookies.set('token', response.data.token, '7d')
                            this.$router.push('/home')
                        }
                        else {
                            $.each(response.data.msg, (index,obj) => {
                                setTimeout(() => {alert(obj[0])},400)
                                setTimeout(() => {this.$router.push('/register')},600)
                            })
                        }
                    })
                }
            }
        }
    }
</script>


<style scoped>
    .login {
        width: 1510px;
        height: 726px;
        position: relative;
        display: inline-block;
        background: url(../assets/img/w.jpg);
        background-size: 100% auto;
        background-repeat: no-repeat;
    }

    h1 {
        color: #fff;
    }

    .div1 {
        width: 30%;
        height: auto;
        margin: 0 auto;
        margin-top: 13%;
        padding: 20px 50px;
        text-align: center;
        background: #00000060;
    }

    .div2 {
        margin-top: 15px;
    }

    .label1 {
        width: 180px;
        color: #fff;
        font-size: 18px;
        padding: 5px 10px;
        border: 0;
        border-bottom: 2px solid #fff;
        background: #ffffff00;
    }

    .label2 {
        width: 190px;
        height: 30px;
        color: #fff;
        font-size: 20px;
        font-weight: 700;
        margin-top: 20px;
        border: 0;
        border-radius: 15px;
        background-image: linear-gradient(to right, #74ebd5 0%, #9face6 100%);
    }
</style>