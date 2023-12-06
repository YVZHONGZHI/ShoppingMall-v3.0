<template>
    <div class="vip" v-if="isLoading">
        <div class="div1">
            <img src="../assets/img/w1.jpg" width="1300" height="260" alt="顶图">
        </div>
        <div class="div2">
            <div class="div3">
                <h1>
                    <label for="w">输入关键字: </label>
                    <input type="text" id="w" name="search" v-model="search">&nbsp;
                    <input type="button" value="搜索" @click="test">
                </h1>
                <h2>产 品 分 类</h2>
                <input type="button" :value="String.fromCharCode(9762) + '   华为                '" class="label1" @click="goPage('/site/' + goods_list[1].site_name + '/tag/' + goods_list[1].tags[0].id)">
                <input type="button" :value="String.fromCharCode(9775) + '   APPLE               '" class="label1" @click="goPage('/site/' + goods_list[6].site_name + '/tag/' + goods_list[6].tags[0].id)">
                <input type="button" :value="String.fromCharCode(9752) + '   三星                '" class="label1" @click="goPage('/site/' + goods_list[2].site_name + '/tag/' + goods_list[2].tags[0].id)">
                <input type="button" :value="String.fromCharCode(9798) + '   OPPO                '" class="label1" @click="goPage('/site/' + goods_list[3].site_name + '/tag/' + goods_list[3].tags[0].id)">
                <input type="button" :value="String.fromCharCode(9910) + '   真我                '" class="label1" @click="goPage('/site/' + goods_list[7].site_name + '/tag/' + goods_list[7].tags[0].id)">
                <input type="button" :value="String.fromCharCode(9878) + '   IQOO                '" class="label1" @click="goPage('/site/' + goods_list[4].site_name + '/tag/' + goods_list[4].tags[0].id)">
            </div>
            <div class="div4">
            <input type="button" value="最新商品" class="label2" @click="goPage('/home')">
            <input type="button" value="推荐商品" class="label3" @click="text">
            </div>
            <div class="div5">
                <table>
                    <tr>
                        <th colspan="1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
                        <th colspan="10">
                            <img :src="goods_list[0].shop_picture" width="110" height="110" alt="">
                        </th>
                        <th colspan="1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
                        <th colspan="10">
                            <img :src="goods_list[1].shop_picture" width="110" height="110" alt="">
                        </th>
                        <th colspan="1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
                        <th colspan="10">
                            <img :src="goods_list[2].shop_picture" width="110" height="110" alt="">
                        </th>
                        <th colspan="1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
                        <th colspan="10">
                            <img :src="goods_list[3].shop_picture" width="110" height="110" alt="">
                        </th>
                        <th colspan="1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
                        <th colspan="10">
                            <img :src="goods_list[4].shop_picture" width="110" height="110" alt="">
                        </th>
                        <th colspan="1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
                    </tr>
                    <tr>
                        <th colspan="1">&nbsp;</th>
                        <th colspan="10">
                            <a :href="'/site/' + goods_list[0].site_name + '/goods/' + goods_list[0].id">
                                <span>{{ goods_list[0].shop_name }}</span>
                            </a>
                        </th>
                        <th colspan="1">&nbsp;</th>
                        <th colspan="10">
                            <a :href="'/site/' + goods_list[1].site_name + '/goods/' + goods_list[1].id">
                                <span>{{ goods_list[1].shop_name }}</span>
                            </a>
                        </th>
                        <th colspan="1">&nbsp;</th>
                        <th colspan="10">
                            <a :href="'/site/' + goods_list[2].site_name + '/goods/' + goods_list[2].id">
                                <span>{{ goods_list[2].shop_name }}</span>
                            </a>
                        </th>
                        <th colspan="1">&nbsp;</th>
                        <th colspan="10">
                            <a :href="'/site/' + goods_list[3].site_name + '/goods/' + goods_list[3].id">
                                <span>{{ goods_list[3].shop_name }}</span>
                            </a>
                        </th>
                        <th colspan="1">&nbsp;</th>
                        <th colspan="10">
                            <a :href="'/site/' + goods_list[4].site_name + '/goods/' + goods_list[4].id">
                                <span>{{ goods_list[4].shop_name }}</span>
                            </a>
                        </th>
                        <th colspan="1">&nbsp;</th>
                    </tr>
                    <tr>
                        <th colspan="1">&nbsp;</th>
                        <th colspan="10">￥{{ parseInt(goods_list[0].shop_price) }}/{{ goods_list[0].tags[0].name }}</th>
                        <th colspan="1">&nbsp;</th>
                        <th colspan="10">￥{{ parseInt(goods_list[1].shop_price) }}/{{ goods_list[1].tags[0].name }}</th>
                        <th colspan="1">&nbsp;</th>
                        <th colspan="10">￥{{ parseInt(goods_list[2].shop_price) }}/{{ goods_list[2].tags[0].name }}</th>
                        <th colspan="1">&nbsp;</th>
                        <th colspan="10">￥{{ parseInt(goods_list[3].shop_price) }}/{{ goods_list[3].tags[0].name }}</th>
                        <th colspan="1">&nbsp;</th>
                        <th colspan="10">￥{{ parseInt(goods_list[4].shop_price) }}/{{ goods_list[4].tags[0].name }}</th>
                        <th colspan="1">&nbsp;</th>
                    </tr>
                </table>
            </div>
            <div class="div6">
                <input type="button" value="特色商品" class="label2" @click="goPage('/exhibit')">
            </div>
            <div class="div7">
                <table>
                    <tr>
                        <th colspan="1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
                        <th colspan="10">
                            <img :src="goods_list[5].shop_picture" width="110" height="110" alt="">
                        </th>
                        <th colspan="1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
                        <th colspan="10">
                            <img :src="goods_list[6].shop_picture" width="110" height="110" alt="">
                        </th>
                        <th colspan="1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
                        <th colspan="10">
                            <img :src="goods_list[7].shop_picture" width="110" height="110" alt="">
                        </th>
                        <th colspan="1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
                        <th colspan="10">
                            <img :src="goods_list[8].shop_picture" width="110" height="110" alt="">
                        </th>
                        <th colspan="1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
                        <th colspan="10">
                            <img :src="goods_list[9].shop_picture" width="110" height="110" alt="">
                        </th>
                        <th colspan="1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</th>
                    </tr>
                    <tr>
                        <th colspan="1">&nbsp;</th>
                        <th colspan="10">
                            <a :href="'/site/' + goods_list[5].site_name + '/goods/' + goods_list[5].id">
                                <span>{{ goods_list[5].shop_name }}</span>
                            </a>
                        </th>
                        <th colspan="1">&nbsp;</th>
                        <th colspan="10">
                            <a :href="'/site/' + goods_list[6].site_name + '/goods/' + goods_list[6].id">
                                <span>{{ goods_list[6].shop_name }}</span>
                            </a>
                        </th>
                        <th colspan="1">&nbsp;</th>
                        <th colspan="10">
                            <a :href="'/site/' + goods_list[7].site_name + '/goods/' + goods_list[7].id">
                                <span>{{ goods_list[7].shop_name }}</span>
                            </a>
                        </th>
                        <th colspan="1">&nbsp;</th>
                        <th colspan="10">
                            <a :href="'/site/' + goods_list[8].site_name + '/goods/' + goods_list[8].id">
                                <span>{{ goods_list[8].shop_name }}</span>
                            </a>
                        </th>
                        <th colspan="1">&nbsp;</th>
                        <th colspan="10">
                            <a :href="'/site/' + goods_list[9].site_name + '/goods/' + goods_list[9].id">
                                <span>{{ goods_list[9].shop_name }}</span>
                            </a>
                        </th>
                        <th colspan="1">&nbsp;</th>
                    </tr>
                    <tr>
                        <th colspan="1">&nbsp;</th>
                        <th colspan="10">￥{{ parseInt(goods_list[5].shop_price) }}/{{ goods_list[5].tags[0].name }}</th>
                        <th colspan="1">&nbsp;</th>
                        <th colspan="10">￥{{ parseInt(goods_list[6].shop_price) }}/{{ goods_list[6].tags[0].name }}</th>
                        <th colspan="1">&nbsp;</th>
                        <th colspan="10">￥{{ parseInt(goods_list[7].shop_price) }}/{{ goods_list[7].tags[0].name }}</th>
                        <th colspan="1">&nbsp;</th>
                        <th colspan="10">￥{{ parseInt(goods_list[8].shop_price) }}/{{ goods_list[8].tags[0].name }}</th>
                        <th colspan="1">&nbsp;</th>
                        <th colspan="10">￥{{ parseInt(goods_list[9].shop_price) }}/{{ goods_list[9].tags[0].name }}</th>
                        <th colspan="1">&nbsp;</th>
                    </tr>
                </table>
            </div>
        </div>
    </div>
</template>


<script>
    export default {
        name: "Vip",
        data() {
            return {
                goods_list: [],
                search: '',
                isLoading: false
            }
        },
        created() {
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
                    this.goods_list = response.data
                    this.isLoading = true
                }
            })
        },
        methods: {
            test() {
                if (this.search) {
                    this.$router.push('/home/?search=' + this.search)
                    this.search = ''
                }
                else{
                    alert("关键字不能为空!")
                }
            },
            text() {
                alert("暂  时  缺  货")
            },
            goPage(url_path) {
                this.$router.push(url_path)
            }
        }
    }
</script>


<style scoped>
    table {
        border: 2q solid;
    }

    span {
        color: red;
    }

    img {
        transition: opacity 2s;
    }

    img:hover {
        opacity: 0;
    }

    h1 {
        font-family: "楷体";
        font-size: 18px;
        margin-left: 30px;
        background-color: white;
    }

    h2 {
        font-family: "微软雅黑";
        font-size: 28px;
        background-color: red;
        color: white;
        text-align: center;
    }

    .label1 {
        font-family: "仿宋";
        font-size: 18px;
        background-color: white;
        color: red;
        width: 370px;
        height: 33px;
    }

    .label2 {
        font-family: "微软雅黑";
        font-size: 18px;
        background-color: orange;
        color: white;
        width: 180px;
    }

    .label3 {
        font-family: "微软雅黑";
        font-size: 18px;
        margin-left: 10px;
        background-color: darkgray;
        width: 180px;
    }

    .div1 {
        width: 1300px;
        height: 250px;
        position: relative;
        left: 118px;
        top: 15px;
        display: inline-block;
    }

    .div2 {
        width: 1316px;
        height: 442px;
        position: relative;
        left: 110px;
        top: 15px;
        display: inline-block;
    }

    .div3 {
        width: 370px;
        height: 318px;
        position: absolute;
        left: 8px;
        top: 8px;
        display: inline-block;
    }

    .div4 {
        width: 910px;
        height: 30px;
        position: absolute;
        left: 408px;
        top: 10px;
        display: inline-block;
    }

    .div5 {
        width: 910px;
        height: 172px;
        position: absolute;
        left: 408px;
        top: 47px;
        display: inline-block;
    }

    .div6 {
        width: 910px;
        height: 30px;
        position: absolute;
        left: 408px;
        top: 233px;
        display: inline-block;
    }

    .div7 {
        width: 910px;
        height: 172px;
        position: absolute;
        left: 408px;
        top: 270px;
        display: inline-block;
    }
</style>