<template>
    <div class="left_menu">
        <div class="panel panel-primary">
            <div class="panel-heading">
                <h3 class="panel-title">商品分类</h3>
            </div>
            <div class="panel-body">
                <p v-for="category in category_list">
                    <a :href="'/site/' + category.site_name + '/category/' + category.id">
                        {{ category.name }}({{ category.count_num }})
                    </a>
                </p>
            </div>
        </div>
        <div class="panel panel-danger">
            <div class="panel-heading">
                <h3 class="panel-title">商品标签</h3>
            </div>
            <div class="panel-body">
                <p v-for="tag in tag_list">
                    <a :href="'/site/' + tag.site_name + '/tag/' + tag.id">
                        {{ tag.name }}({{ tag.count_num }})
                    </a>
                </p>
            </div>
        </div>
        <div class="panel panel-info">
            <div class="panel-heading">
                <h3 class="panel-title">日期归档</h3>
            </div>
            <div class="panel-body">
                <p v-for="date in date_list">
                    <a href="">
                        {{ date[0].split('-')[0] + '年' + date[0].split('-')[1] + '月' }}({{ date[1] }})
                    </a>
                </p>
            </div>
        </div>
    </div>
</template>


<script>
    export default {
        name: "LeftMenu",
        props: {
            category_list: [],
            tag_list: [],
            date_list: []
        }
    }
</script>


<style lang="less" scoped>
    @import '~bootstrap/less/bootstrap.less';
</style>