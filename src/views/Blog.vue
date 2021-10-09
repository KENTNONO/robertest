<script>
import LeftNav from '@/components/Blog/LeftNav.vue';
export default {
    components:{
        LeftNav,
    },
    setup(){
      return{}
    }
}
</script>

<template>
    <LeftNav />
    <div class="blogContainer">
      <router-view></router-view>
    </div>
</template>

<style scoped lang="scss">
  @import '~@/assets/scss/_mixins.scss';
  .blogContainer{
    max-width: 960px;
    box-sizing: border-box;
    padding:30px 30px 60px 30px;
    position: relative;
    z-index: 3;
    margin: 0 auto;
    @include breakpoint(m){
      padding:0 30px 60px 30px;
    }
    @include breakpoint(nb){
      flex-wrap: wrap;
    }
  }
</style>