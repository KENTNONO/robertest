<script>
import {useRoute, useRouter} from "vue-router";
import {useStore} from 'vuex';
import { computed, onMounted, ref, watch, watchEffect } from '@vue/runtime-core';
export default {
    setup(){
        const store = useStore();
        const router = useRouter();
        const route = useRoute();
        const navNum = ref(0);

        
        watch(route,(routePath)=>{
            if(routePath.path === '/'){
                navNum.value = 0;
            }else if(routePath.path === '/about'){
                navNum.value = 1;
            }else if(routePath.path === '/blog' || routePath.path.includes('/article')){
                navNum.value = 2;
            }
        });

        const isAbout = computed(()=>{
            return store.getters.isAbout
        });
        
        const isMobileMenu = computed(()=>{
            return store.getters.isMobileMenu;
        });

        const classIdx = computed(()=>{
            return store.getters.classIdx;
        });

        const handMobileMenu = ()=>{
            store.dispatch('handIsMenu');
        };

        const categoryKind = computed(()=>{
            return store.getters.categoryKind;
        });




        const gotoHomeRouter = ()=>{
            store.dispatch('categoryKind','');
            router.push({path:`/`});
            store.dispatch('handIsAboutFalse');
            store.dispatch('classIdx',0);
            if(window.innerWidth < 600){
                store.dispatch('handIsMenu');
            };
        };

        const gotoBlogRouter = ()=>{
            store.dispatch('categoryKind','');
            store.dispatch('handIsAboutFalse');
            router.push({path:`/blog`});
            if(route.path !== '/blog'){
                store.dispatch('classIdx',0);
            }
            if(window.innerWidth < 600){
                store.dispatch('handIsMenu');
            };
        };

        const gotoAboutRouter = ()=>{
            store.dispatch('categoryKind','');
            router.push({path:`/about`});
            store.dispatch('handIsAboutTrue');
            store.dispatch('classIdx',0);
            if(window.innerWidth < 600){
                store.dispatch('handIsMenu');
            }
            
        };

        return {
                gotoAboutRouter,
                gotoHomeRouter,
                isAbout,
                isMobileMenu,
                handMobileMenu,
                gotoBlogRouter,navNum
            }
    }
}
</script>

<template>
  <header>
        <img src="~@/assets/img/logo.svg" class="logo" alt="">
        <div class="mobileBtn" @click="handMobileMenu">
            <div></div>
            <div></div>
            <div></div>
        </div>
        <nav :class="{showNav:isMobileMenu}">
            <a href="javascript:;" @click="gotoHomeRouter" :class="{current:navNum === 0}">作品</a>
            <a href="javascript:;" @click="gotoAboutRouter" :class="{current:navNum === 1}">關於我</a>
            <a href="javascript:;" @click="gotoBlogRouter" :class="{current:navNum === 2}">部落格</a>
        </nav>
    </header>
</template>


<style lang="scss" scoped>
@import '~@/assets/scss/_mixins.scss';
header{
    position: relative;
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    padding: 30px;
    align-items: center;
    z-index: 9;
    .logo{
        width: 130px;
    }
    nav{
        @include breakpoint(m1){
            overflow: hidden;
            height: 0;
            width: $full;
            padding-top: 0;
            transition: 0.5s all;
        }
        a{
            display: inline-block;
            margin-left: 40px;
            letter-spacing: 2px;
            color: $white;
            font-size: 14px;
            font-weight: 300;
            @include breakpoint(m1){
                width: $full;
                height: 50px;
                text-align: center;
                line-height: 50px;
                margin-left: 0;
                background-color: rgba(255,255,255,0.1);
            }
            &:hover{
                text-decoration: underline;
            }
        }
        .current{
            text-decoration: underline;
        }
    }
    .showNav{
        @include breakpoint(m1){
            height: 100px;
            padding-top: 30px;
        }
    }
    .mobileBtn{
        display: none;
        width: 20px;
        @include breakpoint(m1){
            display: block;
        }
        div{
            height: 2px;
            background-color: $white;
            margin-bottom: 3px;
            &:last-child{
                margin-bottom: 0;
            }
        }
    }
}
</style>