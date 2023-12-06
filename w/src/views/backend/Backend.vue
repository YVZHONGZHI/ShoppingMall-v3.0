<template>
    <div class="backend" v-if="isLoading">
        <nav class="navbar navbar-inverse">
            <div class="container-fluid">
                <!-- Brand and toggle get grouped for better mobile display -->
                <div class="navbar-header">
                    <a :href="'/site/' + username" class="navbar-brand">{{ site_title }}</a>
                </div>

                <!-- Collect the nav links, forms, and other content for toggling -->
                <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                    <ul class="nav navbar-nav">
                        <li><a href="" @click="goPage('/home')">商品</a></li>
                        <li><a href="" @click="goPage('/vip')">精品推荐</a></li>
                    </ul>
                    <form class="navbar-form navbar-left">
                        <div class="form-group">
                            <label for="search"></label>
                            <input type="text" id="search" class="form-control" placeholder="输入关键字" v-model="search">&nbsp;
                        </div>
                        <input type="button" class="btn btn-default" value="搜索" @click="test">
                    </form>
                    <ul class="nav navbar-nav navbar-right">
                        <li v-if="token"><a>{{ username }}</a></li>
                        <li class="dropdown" v-if="token">
                            <a class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">更多操作 <span class="caret"></span></a>
                            <ul class="dropdown-menu">
                                <li><a href="" data-toggle="modal" data-target=".bs-example-modal-lg">修改密码</a></li>
                                <li><a href="" data-toggle="modal" data-target=".bs-example-modal-sm">修改头像</a></li>
                                <li><a>后台管理</a></li>
                                <li role="separator" class="divider"></li>
                                <li><a href="" @click="logout">退出登录</a></li>
                            </ul>
                            <SetPassword/>
                            <SetAvatar/>
                        </li>
                        <li v-if="!token"><a href="" @click="goPage('/register')">注册</a></li>
                        <li v-if="!token"><a href="" @click="goPage('/login')">登录</a></li>
                    </ul>
                </div><!-- /.navbar-collapse -->
            </div><!-- /.container-fluid -->
        </nav>
        <div class="container-fluid">
            <div class="row">
                <div class="col-md-2">
                    <div class="panel-group" id="accordion" role="tablist" aria-multiselectable="true">
                        <div class="panel panel-default">
                            <div class="panel-heading" role="tab" id="headingOne">
                                <h4 class="panel-title">
                                    <a role="button" data-toggle="collapse" data-parent="#accordion" href="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                                        更多操作
                                    </a>
                                </h4>
                            </div>
                            <div id="collapseOne" class="panel-collapse collapse in" role="tabpanel" aria-labelledby="headingOne">
                                <div class="panel-body">
                                    <a href="" @click="goPage('/add_goods')">发售商品</a>
                                </div>
                            </div>
                            <div id="collapseOne" class="panel-collapse collapse in" role="tabpanel" aria-labelledby="headingOne">
                                <div class="panel-body">
                                    <a href="">联系客服</a>
                                </div>
                            </div>
                            <div id="collapseOne" class="panel-collapse collapse in" role="tabpanel" aria-labelledby="headingOne">
                                <div class="panel-body">
                                    <a href="">意见反馈</a>
                                </div>
                            </div>
                            <div id="collapseOne" class="panel-collapse collapse in" role="tabpanel" aria-labelledby="headingOne">
                                <div class="panel-body">
                                    <a href="">&nbsp;&nbsp;&nbsp;其他</a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-md-10">
                    <div>

                        <!-- Nav tabs -->
                        <ul class="nav nav-tabs" role="tablist">
                            <li role="presentation" class="active"><a href="#shop_car" aria-controls="shop_car" role="tab" data-toggle="tab">购物车</a></li>
                            <li role="presentation"><a href="#cash_flow" aria-controls="cash_flow" role="tab" data-toggle="tab">流水</a></li>
                            <li role="presentation"><a href="#goods" aria-controls="goods" role="tab" data-toggle="tab">商品</a></li>
                            <li role="presentation"><a href="#vip" aria-controls="vip" role="tab" data-toggle="tab">会员</a></li>
                        </ul>

                        <!-- Tab panes -->
                        <div class="tab-content">
                            <div role="tabpanel" class="tab-pane fade in active" id="shop_car">
                                <table class="table table-hover table-striped">
                                    <thead>
                                        <tr>
                                            <th>&nbsp;&nbsp;商品名称</th>
                                            <th>&nbsp;&nbsp;商品单价</th>
                                            <th>&nbsp;&nbsp;&nbsp;加入购物车时间</th>
                                            <th>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;操作</th>
                                            <th>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;操作</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="goods in car_list">
                                            <td>
                                                <a :href="'/site/' + goods.site_name + '/goods/' + goods.goods_id">
                                                    {{ goods.shop_name }}
                                                </a>
                                            </td>
                                            <td>￥{{ goods.shop_price }}</td>
                                            <td>{{ goods.shop_time.slice(0,19).replace('T',' ') }}</td>
                                            <td>
                                                <button @click="pay(goods.goods_id)">支付订单</button>
                                            </td>
                                            <td>
                                                <button @click="cancel(goods.id)">取消订单</button>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            <div role="tabpanel" class="tab-pane fade" id="cash_flow">
                                <table class="table table-hover table-striped">
                                    <thead>
                                        <tr>
                                            <th>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;交易时间</th>
                                            <th>买入</th>
                                            <th>卖出</th>
                                            <th>商品名称</th>
                                            <th>&nbsp;交易金额</th>
                                            <th>&nbsp;&nbsp;账户余额</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="flow in flow_list">
                                            <td>{{ flow.pay_time.slice(0,19).replace('T',' ') }}</td>
                                            <td>&nbsp;&nbsp;{{ flow.buy_num }}</td>
                                            <td>&nbsp;&nbsp;{{ flow.sell_num }}</td>
                                            <td>
                                                <a :href="'/site/' + flow.site_name + '/goods/' + flow.goods_id">
                                                    {{ flow.shop_name }}
                                                </a>
                                            </td>
                                            <td>￥{{ flow.shop_price }}</td>
                                            <td>￥{{ flow.balance_flow }}</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            <div role="tabpanel" class="tab-pane fade" id="goods">
                                <table class="table table-hover table-striped">
                                    <thead>
                                        <tr>
                                            <th>&nbsp;&nbsp;商品名称</th>
                                            <th>&nbsp;&nbsp;商品单价</th>
                                            <th>点赞数</th>
                                            <th>评论数</th>
                                            <th>操作</th>
                                            <th>操作</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr v-for="goods in goods_list">
                                            <td>
                                                <a :href="'/site/' + goods.site_name + '/goods/' + goods.id">
                                                    {{ goods.shop_name }}
                                                </a>
                                            </td>
                                            <td>￥{{ goods.shop_price }}</td>
                                            <td>&nbsp;&nbsp;&nbsp;&nbsp;{{ goods.up_num }}</td>
                                            <td>&nbsp;&nbsp;&nbsp;&nbsp;{{ goods.comment_num }}</td>
                                            <td>
                                                <a>编辑</a>
                                            </td>
                                            <td>
                                                <a>删除</a>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            <div role="tabpanel" class="tab-pane fade" id="vip">
                                <table class="table table-hover table-striped">
                                    <thead>
                                        <tr>
                                            <th></th>
                                            <th>会员价格</th>
                                            <th>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;会员权益</th>
                                            <th>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;操作</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <td>限时免费会员</td>
                                            <td>&nbsp;&nbsp;&nbsp;￥&nbsp;0</td>
                                            <td>更多精品推荐与特色商品等你选购</td>
                                            <td>
                                                <button @click="vip">支付订单</button>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
    import SetAvatar from "../../components/SetAvatar";
    import SetPassword from "../../components/SetPassword";
    export default {
        name: "Backend",
        data() {
            return {
                username: '',
                site_title: '',
                car_list: [],
                flow_list: [],
                goods_list: [],
                search: '',
                token: '',
                isLoading: false
            }
        },
        created() {
            this.username = this.$cookies.get('username')
            this.token = this.$cookies.get('token')
            this.site_title = this.$cookies.get('username') + '的网店'
            this.$axios.get(this.$settings.base_url+'/backend/'+this.$cookies.get('username')+'/', {headers: {Authorization: 'JWT '+this.$cookies.get('token')}}).then(response => {
                if (response.data.result) {
                    setTimeout(() => {alert('请先登录才能进入')},400)
                    setTimeout(() => {this.$router.push('/login')},600)
                }
                else {
                    this.car_list = response.data.car_list
                    this.flow_list = response.data.flow_list
                    this.goods_list = response.data.goods_list
                    this.isLoading = true
                }
            })
        },
        methods: {
            logout() {
                this.$cookies.remove('username')
                this.$cookies.remove('token')
                this.username = ''
                this.token = ''
            },
            test() {
                if (this.search) {
                    this.$router.push('/home/?search=' + this.search)
                    this.search = ''
                }
                else{
                    alert("关键字不能为空!")
                }
            },
            pay(goods_id) {
                this.$axios.post(this.$settings.base_url+'/pay/', {
                    username: this.username,
                    goods_id: goods_id
                }).then(response => {
                    if (response.data.code) {
                        window.location.reload()
                        alert(response.data.msg)
                    }
                    else {
                        $.each(response.data.msg, (index,obj) => {
                            alert(obj[0])
                        })
                    }
                })
            },
            cancel(pk) {
                this.$axios.delete(this.$settings.base_url+'/cancel/'+pk+'/').then(() => {
                    window.location.reload()
                    alert('取消订单成功')
                })
            },
            vip() {
                let formDateObj = new FormData();
                formDateObj.append('username', this.username);
                this.$axios.put(this.$settings.base_url+'/vip/'+this.username+'/', formDateObj).then(response => {
                    if (response.data.code) {
                        alert(response.data.msg)
                    }
                    else {
                        $.each(response.data.msg, (index,obj) => {
                            alert(obj[0])
                        })
                    }
                })
            },
            goPage(url_path) {
                this.$router.push(url_path)
            }
        },
        components: {
            SetPassword,
            SetAvatar
        }
    }
</script>


<style lang="less" scoped>
    @import '~bootstrap/less/bootstrap.less';

    .backend {
        font-size: 14px;
        line-height: 1.42857143;
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    }
</style>