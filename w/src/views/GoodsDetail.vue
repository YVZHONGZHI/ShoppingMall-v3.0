<template>
    <div class="goods_detail" v-if="isLoading">
        <nav class="navbar navbar-inverse">
            <div class="container-fluid">
                <!-- Brand and toggle get grouped for better mobile display -->
                <div class="navbar-header">
                    <a :href="'/site/' + goods_obj.site_name" class="navbar-brand">{{ goods_obj.left_menu.site_title }}</a>
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
                                <li><a href="" @click="goPage('/backend')">后台管理</a></li>
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
                <div class="col-md-3">
                    <LeftMenu :category_list="category_list" :tag_list="tag_list" :date_list="date_list"/>
                </div>
                <div class="col-md-9">
                    <h1>
                        {{ goods_obj.shop_name }}
                    </h1>
                    <h2>
                        ￥{{ goods_obj.shop_price }}
                    </h2>
                    <div class="media-left">
                        <img class="media-object" :src="goods_obj.shop_picture" width="125" height="125" alt="商品图片">
                    </div>
                    <div class="media-body" v-html="goods_obj.content"></div>
                    <div class="clearfix">
                        <div id="div_digg">
                            <div class="diggword" ref="shop_car" id="car_tips" style="color: red"></div>
                            <button class="btn btn-primary" @click="shop_car">&nbsp;&nbsp;&nbsp;&nbsp;加入购物车&nbsp;&nbsp;&nbsp;&nbsp;</button>
                            <div class="diggit" @click="up_or_down(true)">
                                <span class="diggnum" id="digg_count">
                                    {{ up_num }}
                                </span>
                            </div>
                            <div class="buryit" @click="up_or_down(false)">
                                <span class="burynum" id="bury_count">
                                    {{ down_num }}
                                </span>
                            </div>
                            <div class="clear"></div>
                            <div class="diggword" ref="up_or_down" id="digg_tips" style="color: red"></div>
                        </div>
                    </div>
                    <div>
                        <ul class="list-group" ref="comment">
                            <li class="list-group-item" v-for="(comment, index) in comment_list">
                                <span>
                                    第{{ index + 1 }}楼
                                </span>
                                <span>
                                    &nbsp;·&nbsp;&nbsp;{{ comment.content_time.slice(0,19).replace('T',' ') }}
                                </span>
                                <span>
                                    &nbsp;·&nbsp;&nbsp;{{ comment.username }}
                                </span>
                                <span>
                                    <br>
                                    <br>
                                    <a class="pull-right" @click="reply(comment.username, comment.id)">回复</a>
                                </span>
                                <div>
                                    <p v-if="comment.parent">@&nbsp;{{ comment.parent }}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{{ comment.content }}</p>
                                    <p v-if="!comment.parent">{{ comment.content }}</p>
                                </div>
                            </li>
                        </ul>
                    </div>
                    <div v-if="token">
                        <p>
                            <span class="glyphicon glyphicon-comment"></span>发表评论
                        </p>
                        <div>
                            <label for="id_comment"></label>
                            <textarea name="comment" id="id_comment" ref="id_comment" cols="60" rows="10" v-model="content"></textarea>
                        </div>
                        <button class="btn btn-primary" @click="comment">提交评论</button>
                        <span ref="comment_error"></span>
                    </div>
                    <li v-if="!token"><a href="" @click="goPage('/register')">注册</a></li>
                    <li v-if="!token"><a href="" @click="goPage('/login')">登录</a></li>
                </div>
            </div>
        </div>
    </div>
</template>


<script>
    import LeftMenu from "../components/LeftMenu";
    import SetAvatar from "../components/SetAvatar";
    import SetPassword from "../components/SetPassword";
    export default {
        name: "GoodsDetail",
        data() {
            return {
                username: '',
                category_list: [],
                tag_list: [],
                date_list: [],
                goods_obj: [],
                comment_list: [],
                search: '',
                up_num: '',
                down_num: '',
                content: '',
                parent_id: '',
                token: '',
                isLoading: false
            }
        },
        created() {
            this.username = this.$cookies.get('username')
            this.token = this.$cookies.get('token')
            this.$axios.get(this.$settings.base_url+'/goods_detail/?mall__site_name='+this.$route.params.username+'&id='+this.$route.params.goods_id).then(response => {
                if (response.data.length) {
                    this.goods_obj = response.data[0]
                    this.category_list = response.data[0].left_menu.category_list
                    this.tag_list = response.data[0].left_menu.tag_list
                    this.date_list = response.data[0].left_menu.date_list
                    this.comment_list = response.data[0].comment
                    this.up_num = response.data[0].up_num
                    this.down_num = response.data[0].down_num
                    this.isLoading = true
                }
                else {
                    this.$router.push('/errors')
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
            shop_car() {
                this.$axios.post(this.$settings.base_url+'/shop_car/', {
                    username: this.username,
                    goods_id: this.goods_obj.id
                }).then(response => {
                    if (response.data.code) {
                        this.$refs.shop_car.textContent = response.data.msg
                    }
                    else {
                        $.each(response.data.msg, (index,obj) => {
                            this.$refs.shop_car.innerHTML = obj[0]
                        })
                    }
                })
            },
            up_or_down(isUp) {
                this.$axios.put(this.$settings.base_url+'/up_or_down/'+this.goods_obj.id+'/', {
                    username: this.username,
                    is_up: isUp
                }).then(response => {
                    if (response.data.code) {
                        this.$refs.up_or_down.textContent = response.data.msg
                        if (isUp) {
                            this.up_num += 1
                        }
                        else {
                            this.down_num += 1
                        }
                    }
                    else {
                        $.each(response.data.msg, (index,obj) => {
                            this.$refs.up_or_down.innerHTML = obj[0]
                        })
                    }
                })
            },
            comment() {
                let username = this.username
                let content = this.content
                if (this.parent_id) {
                    let indexNum = content.indexOf('\n') + 1
                    content = content.slice(indexNum)
                }
                this.$axios.post(this.$settings.base_url+'/comment/', {
                    username: username,
                    goods_id: this.goods_obj.id,
                    content: content,
                    parent_id: this.parent_id
                }).then(response => {
                    if (response.data.code) {
                        this.content = ''
                        this.$nextTick(() => {
                            let temp = `<li class="list-group-item">
                                            <span>最新评论</span>
                                            <span>&nbsp;·&nbsp;&nbsp;${response.data.msg}</span>
                                            <span>&nbsp;·&nbsp;&nbsp;${username}</span>
                                            <span>
                                                <br>
                                                <br>
                                                <a class="pull-right">回复</a>
                                            </span>
                                            <div>${content}</div>
                                        </li>`
                            this.$refs.comment.insertAdjacentHTML('beforeend',temp)
                        })
                        this.parent_id = ''
                    }
                    else {
                        $.each(response.data.msg, (index,obj) => {
                            this.$refs[index].innerHTML = obj[0]
                        })
                    }
                })
            },
            reply(commentUserName, parentId) {
                this.parent_id = parentId
                let newContent = '@ ' + commentUserName + '\n'
                this.$refs.id_comment.textContent = newContent
                this.$refs.id_comment.focus()
                this.$refs.id_comment.setSelectionRange(newContent.length, newContent.length)
            },
            goPage(url_path) {
                this.$router.push(url_path)
            }
        },
        components: {
            SetPassword,
            SetAvatar,
            LeftMenu
        }
    }
</script>


<style lang="less" scoped>
    @import '~bootstrap/less/bootstrap.less';

    .goods_detail {
        font-size: 14px;
        line-height: 1.42857143;
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
    }

    #div_digg {
        float: right;
        margin-bottom: 10px;
        margin-right: 30px;
        font-size: 12px;
        width: 128px;
        text-align: center;
        margin-top: 10px;
    }

    .diggit {
        float: left;
        width: 46px;
        height: 52px;
        background: url(../assets/img/w1.gif) no-repeat;
        text-align: center;
        cursor: pointer;
        margin-top: 2px;
        padding-top: 5px;
    }

    .buryit {
        float: right;
        margin-left: 20px;
        width: 46px;
        height: 52px;
        background: url(../assets/img/w.gif) no-repeat;
        text-align: center;
        cursor: pointer;
        margin-top: 2px;
        padding-top: 5px;
    }

    .clear {
        clear: both;
    }
</style>