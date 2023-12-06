<template>
    <div class="exhibit" v-if="isLoading">
        <fieldset>
            <legend>旗舰5G平板</legend>
            <table>
                <tr>
                    <th>
                        <img src="../assets/img/w2.jpg" width="686" height="400" alt="展示图">
                    </th>
                </tr>
                <tr>
                    <th>
                        <h1>
                            ￥{{ parseInt(goods_list.shop_price) }}
                            <input type="button" value="多款可选" @click="check">
                        </h1>
                    </th>
                </tr>
                <tr>
                    <th>
                        <a href="" class="span1">赠送积分</a>
                    </th>
                </tr>
                <tr><th>&nbsp;</th></tr>
                <tr>
                    <th>
                        <span class="span2">
                            {{ goods_list.up_num + goods_list.down_num }}人评价&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{ goods_list.up_num + goods_list.down_num === 0 ? '100' : Math.round((goods_list.up_num / (goods_list.up_num + goods_list.down_num)) * 100) }}%好评
                        </span>
                    </th>
                </tr>
                <tr>
                    <th>
                        <span class="span3" ref="password_error">&nbsp;</span>
                    </th>
                </tr>
                <tr>
                    <th>
                        <label for="p">输入账号密码: </label>
                        <input type="password" id="p" name="password" v-model="password" @focus="focus('password_error')">&nbsp;
                        <input type="button" value="立  即  购  买" @click="exhibit">
                    </th>
                </tr>
            </table>
        </fieldset>
    </div>
</template>


<script>
    export default {
        name: "Exhibit",
        data() {
            return {
                goods_list: [],
                username: '',
                password: '',
                isLoading: false
            }
        },
        created() {
            this.username = this.$cookies.get('username')
            this.$axios.get(this.$settings.base_url+'/created/', {headers: {Authorization: 'JWT '+this.$cookies.get('token')}}).then(response => {
                if (response.data.result) {
                    $.each(response.data.result, (index,obj) => {
                        if (obj === '您没有执行该操作的权限。') {
                            setTimeout(() => {alert('请先购买会员才能进入')},400)
                            setTimeout(() => {this.$router.push('/home')},600)
                        }
                        else {
                            setTimeout(() => {alert('请先登录才能进入')},400)
                            setTimeout(() => {this.$router.push('/login')},600)
                        }
                    })
                }
                else {
                    this.goods_list = response.data[10]
                    this.isLoading = true
                }
            })
        },
        methods: {
            check() {
                alert("暂  时  缺  货")
            },
            exhibit() {
                this.$axios.post(this.$settings.base_url+'/exhibit/', {
                    username: this.username,
                    password: this.password
                }).then(response => {
                    if (response.data.code) {
                        let confirm_password = prompt("再次确认账号密码")
                        if (confirm_password) {
                            if (confirm_password === this.password) {
                                this.$refs.password_error.textContent = '\xa0'
                                setTimeout(() => {alert(response.data.msg)},400)
                                setTimeout(() => {this.$router.push('/home')},600)
                            }
                            else {
                                this.$refs.password_error.textContent = "两次输入的账号密码不一致!"
                            }
                        }
                        else {
                            this.$refs.password_error.textContent = "账号密码不能为空!"
                        }
                    }
                    else {
                        $.each(response.data.msg, (index,obj) => {
                            this.$refs.password_error.textContent = obj[0]
                        })
                    }
                })
            },
            focus(error) {
                this.$refs[error].textContent = '\xa0'
            }
        }
    }
</script>


<style scoped>
    fieldset {
        height: 683px;
    }

    table {
        margin: auto;
        border-collapse: collapse;
    }

    h1 {
        color: red;
        font-size: 48px;
    }

    img {
        transition: opacity 2s;
    }

    img:hover {
        opacity: 0;
    }

    .span1 {
        color: red;
    }

    .span2 {
        color: darkgray;
    }

    .span3 {
        color: red;
        font-size: 13px;
        font-family: "微软雅黑 Light";
    }
</style>