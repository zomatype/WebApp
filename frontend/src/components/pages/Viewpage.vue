<template>
    <div class="uploaded-scores">
        <h1>アップロードした楽譜一覧</h1>
        <ul>
            <li v-for="(score, index) in uploadedScores" :key="index">
                <a :href="score.url" :download="score.name">{{ score.name }}</a>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    name: 'PreviewList'
}

</script>

<style scoped>
.uploaded-scores {
    padding: 20px;
}

h1 {
    margin-bottom: 20px;
}

ul {
    list-style: none;
    padding: 0;
}

li {
    margin-bottom: 10px;
}
</style>
