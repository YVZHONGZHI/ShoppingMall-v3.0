<template>
    <div class="set_avatar">
        <!-- Small modal -->

        <div class="modal fade bs-example-modal-sm" tabindex="-1" role="dialog" aria-labelledby="mySmallModalLabel">
            <div class="modal-dialog modal-sm" role="document">
                <div class="modal-content">
                    <h1 class="text-center">修改头像</h1>
                    <div class="row">
                        <div class="col-md-8 col-md-offset-2">
                            <div class="form-group">
                                <label for="myfile">
                                    原头像:&nbsp;&nbsp;&nbsp;&nbsp;<img :src="old_avatar" width="75" height="75" alt="原用户名图标">
                                </label>
                            </div>
                            <div class="form-group">
                                <label for="avatar">
                                    新头像:&nbsp;&nbsp;&nbsp;&nbsp;<img src="../assets/img/w3.jpg" ref="myimg" width="75" height="75" alt="新用户名图标">
                                </label>
                                <input type="file" id="avatar" name="avatar" style="display: none" @change="avatarChange">
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-default" data-dismiss="modal">取消</button>
                                <button id="set_avatar" class="btn btn-primary" @click="set_avatar">提交</button>
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
        name: "SetAvatar",
        data() {
            return {
                username: '',
                old_avatar: '',
                new_avatar: ''
            }
        },
        created() {
            this.username = this.$cookies.get('username')
            if (this.username) {
                this.$axios.get(this.$settings.base_url+'/set_avatar/'+this.$cookies.get('username')+'/').then(response => {
                    this.old_avatar = response.data.avatar
                })
            }
        },
        methods: {
            avatarChange(event) {
                let myFileReaderObj = new FileReader();
                this.new_avatar = event.target.files[0];
                myFileReaderObj.readAsDataURL(this.new_avatar)
                myFileReaderObj.onload = () => {
                    this.$refs.myimg.src = myFileReaderObj.result
                }
            },
            set_avatar() {
                let formDateObj = new FormData();
                formDateObj.append('avatar', this.new_avatar);
                this.$axios.put(this.$settings.base_url+'/set_avatar/'+this.username+'/', formDateObj).then(() => {
                    alert('修改成功')
                    window.location.reload()
                })
            }
        }
    }
</script>


<style lang="less" scoped>
    @import '~bootstrap/less/bootstrap.less';
</style>