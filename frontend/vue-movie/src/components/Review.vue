<template>
    <div>
        <h2>Отзывы</h2>
        <div v-for="review in reviews" :key="review.id">
            <h6>{{review.name}}</h6>
            <p v-html="review.text"></p>
            <a href="#formReview" @click="addParent(review.id)">Ответить</a>
            <div v-for="child in review.children" :key="child.id">
                <h6>{{child.name}}</h6>
                <p v-html="child.text"></p>
            </div>
        </div>

        <form action="#" method="get" id="formReview">
            <label for="contactcomment">Ваш комментарий</label>
            <textarea id="contactcomment" cols="30" rows="10" v-model="text">
            </textarea>

            <label for="contactusername">Ваше имя</label>
            <input id="contactusername" v-model="name">

            <label for="contactemail">Ваш email</label>
            <input id="contactemail" v-model="email">

            <button type="button" @click="sendReview()">
                Отправить
            </button>
        </form>
    </div>
</template>

<script>
export default {
    name: 'Review',
    props: ['reviews', 'movie'],
    data() {
        return {
            name: '',
            email: '',
            text: '',
            parent: null,
        }
    },
    methods: {
        async sendReview() {
            let data = {
                name: this.name,
                email: this.email,
                text: this.text,
                parent: this.parent,
                movie: this.movie
            }
            fetch(
            `${this.$store.getters.getServerUrl}/review/`,
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            }
            ).then(() => {
                this.$emit('reLoad')
                this.clearForm()
                })
        },
        addParent(id) {
            this.parent = id
        },
        clearForm() {
            this.name = ''
            this.email = ''
            this.text = ''
            this.parent = null
        }
    }
}
</script>

<style>

</style>