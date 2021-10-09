<script>
import { computed, ref } from '@vue/reactivity';
import {useStore} from 'vuex';
import {useRouter} from 'vue-router';
export default {
  setup(){
    const store = useStore();
    const tagParent = ref(null);
    const router = useRouter();

    const categoryArr = computed(()=>{
      return store.getters.categoryArr;
    });

    const categoryKind = computed(()=>{
      return store.getters.categoryKind;
    });

    const classIdx = computed(()=>{
      return store.getters.classIdx;
    });

    const handAll = (classNum)=>{
      store.dispatch('classIdx',classNum);
      store.dispatch('categoryKind','');
      store.dispatch('handCategoryArr',categoryKind.value);
      router.push({path:`/blog`});
      
    };

    const handKnowledge = (classNum)=>{
        router.push({path:"/blog"});
        store.dispatch('classIdx',classNum);
        store.dispatch('categoryKind','網頁知識');
        store.dispatch('handCategoryArr',categoryKind.value);
    };

    const handShare = (classNum)=>{
      router.push({path:"/blog"});
      store.dispatch('classIdx',classNum);
      store.dispatch('categoryKind','網頁技術分享');
      store.dispatch('handCategoryArr',categoryKind.value);
    }

    const handMovie = (classNum)=>{
      router.push({path:"/blog"});
      store.dispatch('classIdx',classNum);
      store.dispatch('categoryKind','電影哈拉');
      store.dispatch('handCategoryArr',categoryKind.value);
    }

    const handNBA = (classNum)=>{
      router.push({path:'/blog'});
      store.dispatch('classIdx',classNum);
      store.dispatch('categoryKind','NBA反指標');
      store.dispatch('handCategoryArr',categoryKind.value);
    }

    const handLife = (classNum)=>{
      router.push({path:'/blog'});
      store.dispatch('classIdx',classNum);
      store.dispatch('categoryKind','生活來打屁');
      store.dispatch('handCategoryArr',categoryKind.value);
    }

    return{handAll,handKnowledge,handShare,handMovie,handNBA,handLife,classIdx}
  }
}
</script>

<template>
  <aside class="leftNav">
    <h1>部落格</h1>
    <ul>
      <li><a href="javascript:;" @click="handAll(0)" :class="{current:classIdx==0}">全部文章</a></li>
      <li><a href="javascript:;" @click="handKnowledge(1)" :class="{current:classIdx==1}">網頁知識</a></li>
      <li><a href="javascript:;" @click="handShare(2)" :class="{current:classIdx==2}">網頁技術分享</a></li>
      <li><a href="javascript:;" @click="handMovie(3)" :class="{current:classIdx==3}">電影哈拉</a></li>
      <li><a href="javascript:;" @click="handNBA(4)" :class="{current:classIdx==4}">NBA反指標</a></li>
      <li><a href="javascript:;" @click="handLife(5)" :class="{current:classIdx==5}">生活來打屁</a></li>
    </ul>
  </aside>
</template>

<style scoped lang="scss">
@import '~@/assets/scss/_mixins.scss';
.leftNav{
  width:225px;
  margin-left: 27px;
  position: fixed;
  z-index: 3;
  padding-top: 20px;
  @include breakpoint(nb){
    width:calc(100% - 60px);
    margin-left: 30px;
    position: relative;
  }
  h1{
    font-size: 30px;
    font-weight: 400;
    color: $white;
    letter-spacing: 3px;
  }
  ul{
    margin-top: 20px;
    @include breakpoint(nb){
      margin-top: 0;
      white-space: nowrap;
      overflow: auto;
    }
    li{
      display: block;
      margin-top: 18px;
      @include breakpoint(nb){
        display: inline-block;
        width: 120px;
        margin-right: 10px;
      }
      a{
        color: $white;
        font-weight: 100;
        font-size: 16px;
        display: block;
        letter-spacing: 1px;
        transition: 0.2s all;
        @include breakpoint(nb){
          border: 1px solid $white;
          padding:5px 0;
          text-align: center;
        }
        &:hover{
          text-decoration: underline;
        }
      }
    }
    .current{
      text-decoration: underline;
      font-weight: 400;
      @include breakpoint(nb){
        background-color: $white;
        color: $gray;
        text-decoration: none;
      }
    }
  }
}
</style>