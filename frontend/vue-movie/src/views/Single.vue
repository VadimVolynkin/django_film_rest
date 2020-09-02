<template>
    <div class="single">
        <h1>{{movie.name}}</h1>
        <img :src="movie.poster" style="width:200px;">
        <p v-html="movie.description"></p>
        <span><b>Режиссеры:</b> 
            <span v-for="actor in movie.actors" :key="actor.id">{{ actor.name }}</span>
        </span>
        <span><b>Жанры:</b> 
            <span v-for="genre in movie.genres" :key="genre">{{ genre }}</span>
        </span>
        <Review :reviews="movie.reviews" :movie="movie.id" @reLoad="loadMovie" />
    </div>
</template>

<script>
import Review from "../components/Review";
export default {
    name: "Single",
    props: ['id'],
    components: {Review},
    data() {
        return {
            movie: {}
        }
    },
    created() {
        this.loadMovie()
    },
    methods: {
        async loadMovie() {
            this.movie = await fetch(
            `${this.$store.getters.getServerUrl}/movie/${this.id}`
        ).then(response => response.json())
        console.log(this.movie)
        console.log(this.id)
        console.log(this.state)
        }
    }
}
</script>

<style>

</style>