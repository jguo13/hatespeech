import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export const store = new Vuex.Store({
  state: {
    scrapedDomain: '',
    loadingStatus: false
  },
  mutations: {
  	loadingStatus (state, newLoadingStatus) {
  		state.loadingStatus = newLoadingStatus
  	},
    change(state, scrapedDomain) {
      state.scrapedDomain = scrapedDomain
    }
  },

  getters: {
  	loadingStatus (state) {
  		return state.loadingStatus
  	},
    scrapedDomain: state => state.scrapedDomain
  },
})
