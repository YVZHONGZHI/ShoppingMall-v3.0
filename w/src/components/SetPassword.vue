<template>
    <div class="set_password">
        <!-- Large modal -->

        <div class="modal fade bs-example-modal-lg" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabel">
            <div class="modal-dialog modal-lg" role="document">
                <div class="modal-content">
                    <h1 class="text-center">修改密码</h1>
                    <div class="row">
                        <div class="col-md-8 col-md-offset-2">
                            <div class="form-group">
                                <label for="username">用户名</label>
                                <input type="text" id="username" :value="username" class="form-control" disabled>
                            </div>
                            <div class="form-group">
                                <label for="id_old_password">原密码</label>
                                <input type="password" id="id_old_password" class="form-control" v-model="old_password">
                            </div>
                            <div class="form-group">
                                <label for="id_new_password">新密码</label>
                                <input type="password" id="id_new_password" class="form-control" v-model="new_password">
                            </div>
                            <div class="form-group">
                                <label for="id_confirm_password">确认密码</label>
                                <input type="password" id="id_confirm_password" class="form-control" v-model="confirm_password">
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
                                <button id="set_password" class="btn btn-primary" @click="set_password">修改</button>
                                <span style="color: red" ref="password_error"></span>
                            </div>
                            <br>
                            <br>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
    export default {
        name: "SetPassword",
        data() {
            return {
                username: '',
                old_password: '',
                new_password: '',
                confirm_password: ''
            }
        },
        created() {
            this.username = this.$cookies.get('username')
        },
        methods: {
            set_password() {
                this.$axios.put(this.$settings.base_url+'/set_password/'+this.username+'/', {
                    username: this.username,
                    old_password: this.old_password,
                    new_password: this.new_password,
                    confirm_password: this.confirm_password
                }).then(response => {
                    if (response.data.code) {
                        alert(response.data.msg)
                        window.location.reload()
                    }
                    else {
                        $.each(response.data.msg, (index,obj) => {
                            this.$refs.password_error.textContent = obj[0]
                        })
                    }
                })
            }
        }
    }
</script>


<style lang="less" scoped>
    @import '~bootstrap/less/bootstrap.less';
</style>