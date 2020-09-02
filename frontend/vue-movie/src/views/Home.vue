<template>
  <div class="home">
    <div v-for="movie in listMovie" :key="movie.id">
      <a :href="movie.id" @click="goTo(movie.id)">{{ movie.name }}</a>
      <img :src="movie.poster" style="width:200px;">
      <p>{{ movie.description }}</p>
    </div>
  </div>
</template>

<script>

export default {
  name: 'Home',
  data() {
    return {
      listMovie: []
    }
  },
  components: {},
  created() {
    this.loadListMovie()
  },
  methods: {
    async loadListMovie() {
      this.listMovie = await fetch(
        `${this.$store.getters.getServerUrl}/movie`
      ).then(response => response.json())
    },
    goTo(id) {
      this.$router.push({ name:'Single', params: {id: id} })
    },
  }
}
</script>
