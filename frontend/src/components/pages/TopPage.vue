<template>
    <div class="home-page">
        <img  src="../../assets/logo.png">
        <h1>App Name</h1>
        <input type="file" @change="handleFileUpload" accept=".pdf"/>
        <b-button disabled size="lg" variant="primary">Upload</b-button>
        <div v-if="uploadedFile">
            <h2>アップロードされた楽譜</h2>
            <img v-if="isImageFile" :src="uploadedFile" alt="アップロードされた楽譜" />
            <iframe v-else :src="uploadedFile" frameborder="0"></iframe>
        </div>
    </div>
</template>
<script>
export default {
    name: 'Home'
}
</script>
<style scoped>
.home-page{
    margin-top: 10%;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
}
h1 {
    margin-bottom: 20px;
}

input[type="file"] {
    margin-bottom: 20px;
}

button {
    margin-bottom: 20px;
}

h2 {
    margin-bottom: 10px;
}

img {
    max-width: 100%;
    max-height: 500px;
    margin-bottom: 10px;
}

iframe {
    width: 100%;
    height: 500px;
    margin-bottom: 10px;
}
</style>
