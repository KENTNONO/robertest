<script>
import { computed, onMounted } from '@vue/runtime-core';
import {useStore} from 'vuex';
import {useRouter} from 'vue-router';
export default {
  setup(){
    const store = useStore();
    const router = useRouter();
  
    const categoryArr = computed(()=>{
      return store.getters.categoryArr;
    });

    const categoryKind = computed(()=>{
      return store.getters.categoryKind;
    });
    

    const blogList = ()=>{
      store.dispatch('handBlogList').then(()=>{
        store.dispatch('handCategoryArr',categoryKind.value);
      });
    };

    onMounted(()=>{
      blogList();
    });

    const linkArticleid = (id)=>{
      router.push({path:`/blog/article/${id}`})
    };

    return {categoryArr,linkArticleid}
  }
}
</script>

<template>

  <div class="listContainer">
    <a href="#" class="addBtn" style="display:none;">新增</a>
    <div class="article">
      <div v-for="item in categoryArr" @click="linkArticleid(item.id)" :key="item.id"  class="list">
        <div class="time">{{item.time}}</div>
        <div class="info">
          <div class="title">{{item.title}}</div>
          <div class="smallTitle">{{item.sub_title}}</div>
        </div>
        <div class="editCon" style="display:none;">
          <a class="edit" href="javascript:;">編</a>
          <a class="push pushClose" href="javascript:;">發</a>
          <a class="delete" href="javascript:;">刪</a>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
@import '~@/assets/scss/_mixins.scss';
.listContainer{
  width: $full;
  @include breakpoint(nb){
    margin-top: 30px;
  }
  .addBtn{
    background-color: $white;
    display: block;
    float: right;
    width: 115px;
    height: 46px;
    border-radius: 3px;
    margin-bottom: 15px;
    text-align: center;
    font-size: 22px;
    line-height: 46px;
  }
  .article{
    clear: both;
    .list{
      width:$full;
      display: flex;
      justify-content: flex-start;
      align-items: flex-start;
      padding-bottom: 30px;
      padding-top: 30px;
      border-bottom: 1px solid rgba(255,255,255,0.2);
      cursor: pointer;
      transition: 0.3s all;
      @include breakpoint(nb){
        flex-wrap: wrap;
      }
      &:hover{
        border-bottom: 10px solid $white;
        padding-bottom: 21px;
      }
      &:first-child{
        padding-top: 0;
      }
      .time{
        width:210px;
        font-size: 14px;
        font-weight: 300;
        color: $white;
      }
      .info{
        width:calc(100% - 105px - 230px);
        @include breakpoint(nb){
          width:calc(100% - 230px);
        }
        @include breakpoint(m1){
          width: $full;
          margin-top: 10px;
        }
        .title{
          font-size: 20px;
          letter-spacing: 1px;
          margin-bottom: 5px;
          color: $white;
          font-weight: 300;
        }
        .smallTitle{
          font-weight: 100;
          font-size: 16px;
          color: $white;
          letter-spacing: 1px;
        }
      }
      .editCon{
        width:105px;
        margin-left: 20px;
        @include breakpoint(nb){
          width:$full;
          margin-left: 0;
          margin-top: 15px;
        }
        a{
          display: inline-block;
          width:30px;
          height: 30px;
          line-height: 30px;
          font-size: 14px;
          color: $gray;
          background-color: $white;
          text-align: center;
          margin: 0 2px;
          border-radius: 2px;
        }
        .delete{
          background-color: red;
          color: $white;
        }
        .pushClose{
          background-color: $gray;
          color: $white;
        }
      }
    }
  }
}
</style>