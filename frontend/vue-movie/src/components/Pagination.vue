<template>
    <div>
        <ul>
            <li v-for="p in totalPages" :key="p">
                <button 
                class="pagination-button"
                :class="{active: currentPage===p}"
                @click="changePage(p)">
                {{p}}
                </button>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    name: "Pagination",
    props: ['total', 'item'],
    data() {
        return {
            currentPage: 1
        }
    },
    computed: {
        totalPages() {
            return Math.ceil(this.total / this.item)
        }
    },
    methods: {
        changePage(pageNumber) {
            this.currentPage = pageNumber
            this.$emit('page-changed', pageNumber)
        }
    }
}
</script>

<style scoped>
.pagination-button{
    color:blue;
}
.active{
    color:red;
}
</style>