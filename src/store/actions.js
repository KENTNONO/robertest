import axios from "axios";

export default {
    blogData({commit},id){
        return axios.get(`http://localhost:3000/datas/${id}`).then((res)=>{
            commit('blogData',res.data);
        }).catch((err)=>{
            return err.response.status;
        });
    },
    classIdx({commit},num){
        commit('classIdx',num)
    },
    handCategoryArr({commit},category){
        const strCategory = category
        commit('handCategoryArr',strCategory)
    },
    handBlogList({commit}){
        return axios.get('http://localhost:3000/datas')
        .then((res)=>{
            commit('handBlogList',res.data);
            return res.data
        })
    },
    categoryKind({commit},kind){
        commit('categoryKind',kind)
    },
    handInit({commit}){
        return axios.get(window.location.href+'api/portfolio.json')
        .then((res)=>{
            commit('init',res.data);
            return res.data.portfolio;
        })
    },
    handIsLoad({commit},bool){
        commit('handIsLoad',bool)
    },
    handIsMenu(context){
        const bool = !context.state.isMobileMenu
        context.commit('handIsMenu',bool)
    },
    handIsAboutFalse(context){
        const bool = false;
        context.commit('handIsAboutFalse',bool)
    },
    handIsAboutTrue(context){
        const bool = true;
        context.commit('handIsAboutTrue',bool)
    },
};