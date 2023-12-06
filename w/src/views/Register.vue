<template>
    <div class="register">
        <div class="div1">
        	  中  文  用  户  注  册  页  面
        </div>
        <div class="div2">
            <form action="" id="w" novalidate>
                <table>
                    <tr>
                        <th colspan="3">
                            <label for="w1">用户名:</label>
                        </th>
                        <th colspan="9">
                            <input type="text" id="w1" name="username" @focus="focus('username_error')">
                        </th>
                        <th colspan="3">
                            <span ref="username_error"></span>
                        </th>
                    </tr>
                    <tr><th>&nbsp;</th></tr>
                    <tr>
                        <th colspan="3">
                            <label for="p">密码:</label>
                        </th>
                        <th colspan="9">
                            <input type="password" id="p" name="password" @focus="focus('password_error')">
                        </th>
                        <th colspan="3">
                            <span ref="password_error"></span>
                        </th>
                    </tr>
                    <tr><th>&nbsp;</th></tr>
                    <tr>
                        <th colspan="3">
                            <label for="p1">确认密码:</label>
                        </th>
                        <th colspan="9">
                            <input type="password" id="p1" name="confirm_password" @focus="focus('confirm_password_error')">
                        </th>
                        <th colspan="3">
                            <span ref="confirm_password_error"></span>
                        </th>
                    </tr>
                    <tr><th>&nbsp;</th></tr>
                    <tr>
                        <th colspan="3">
                            <label for="w2">邮箱:</label>
                        </th>
                        <th colspan="9">
                            <input type="email" id="w2" name="email" @focus="focus('email_error')">
                        </th>
                        <th colspan="3">
                            <span ref="email_error"></span>
                        </th>
                    </tr>
                    <tr><th>&nbsp;</th></tr>
                    <tr>
                        <th colspan="3">
                            <label for="myfile">头像:</label>
                        </th>
                        <th colspan="9">
                            <img src="../assets/img/w3.jpg" ref="avatar" width="75" height="75" alt="用户名图标">
                            <input type="file" id="myfile" name="avatar" style="display: none" @change="avatarChange">
                        </th>
                    </tr>
                    <tr><th colspan="3">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th><th colspan="9">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th><th colspan="3">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th></tr>
                    <tr><th>&nbsp;</th></tr>
                </table>
            </form>
            <table>
                <tr>
                    <th colspan="4">
                        <input type="button" value="提  交" class="label1" @click="register">
                    </th>
                    <th colspan="4">
                        <input type="reset" value="重  置" class="label2" form="w">
                    </th>
                    <th colspan="4">
                        <input type="button" value="重  新  登  录" class="label2" @click="goPage('/login')">
                    </th>
                </tr>
            </table>
        </div>
    </div>
</template>


<script>
    export default {
        name: "Register",
        data() {
            return {avatar: ''}
        },
        methods: {
            avatarChange(event) {
                let myFileReaderObj = new FileReader();
                this.avatar = event.target.files[0];
                myFileReaderObj.readAsDataURL(this.avatar)
                myFileReaderObj.onload = () => {
                    this.$refs.avatar.src = myFileReaderObj.result
                }
            },
            register() {
                let formDateObj = new FormData();
                $.each($('form').serializeArray(), (index, obj) => {
                    formDateObj.append(obj.name, obj.value)
                })
                formDateObj.append('avatar', this.avatar);
                this.$axios.post(this.$settings.base_url+'/register/', formDateObj).then(response => {
                    if (response.data.code) {
                        setTimeout(() => {alert(response.data.msg)},200)
                    }
                    else {
                        $.each(response.data.msg, (index,obj) => {
                            let targetId = index + '_error';
                            this.$refs[targetId].textContent = obj[0]
                        })
                    }
                })
            },
            focus(error) {
                this.$refs[error].textContent = ''
            },
            goPage(url_path) {
                this.$router.push(url_path)
            }
        }
    }
</script>


<style scoped>
    .div1 {
        top: 93px;
        width: 1300px;
        height: 100px;
        z-index: 1;
        font-size: 28px;
        position: relative;
        margin-left: 110px;
        text-align: center;
        font-family: "微软雅黑";
    }

    .div2 {
        top: 85px;
        z-index: 1;
        position: relative;
    }

    table {
        margin-left: 607px;
        border-collapse: collapse;
    }

    span {
        color: red;
        font-size: 13px;
        font-family: "微软雅黑 Light";
    }

    .label1 {
        width: 90px;
        color: white;
        font-size: 13px;
        background-color: blue;
        font-family: "微软雅黑";
    }

    .label2 {
        width: 90px;
        font-size: 13px;
        margin-left: 15px;
        font-family: "微软雅黑";
    }
</style>