<template>
  <div class="home">
    <div v-for="movie in listMovie" :key="movie.id">
      <a :href="movie.id" @click="goTo(movie.id)">{{ movie.name }}</a>
      <img :src="movie.poster" style="width:200px;">
      <p>{{ movie.description }}</p>
    </div>
    <Pagination :total="total" :item="listMovie.length" @page-changed="loadListMovie" />
  </div>
</template>

<script>
import Pagination from "../components/Pagination";

export default {
  name: 'Home',
  data() {
    return {
      listMovie: [],
      page: 1,
      total: 0,
    }
  },
  components: {Pagination},
  created() {
    this.loadListMovie(this.page)
  },
  methods: {
    async loadListMovie(pageNumber) {
      this.listMovie = await fetch(
        `${this.$store.getters.getServerUrl}/movie?page=${pageNumber}`
      ).then(response => response.json()
      ).then(response => {
        this.total = response.count
        return response.results
        })
    },
    goTo(id) {
      this.$router.push({ name:'Single', params: {id: id} })
    },
  }
}
</script>
