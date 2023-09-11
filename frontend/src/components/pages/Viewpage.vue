<template>
    <div class="uploaded-scores">
        <img src="../../assets/logo.png">
        <h1>アップロードした楽譜一覧</h1>
        <ul>
            <li v-for="(score, index) in uploadedScores" :key="index">
                <a :href="score.url" :download="score.name">{{ score.name }}</a>
            </li>
        </ul>
        
        <div v-if="uploadedScores.length === 0">ファイルがアップロードされていません。</div>
    </div>
</template>

<script>
export default {
    name: 'PreviewList',
    data() {
        return {
            uploadedScores: []
        };
    },
    created() {
        this.fetchUploadedScores();
    },
    methods: {
        async fetchUploadedScores() {
            try {
                const response = await fetch('http://127.0.0.1:5000/files');
                if (response.ok) {
                    const data = await response.json();
                    this.uploadedScores = data.files.map(file => ({
                        name: file.filename,
                        url: `http://127.0.0.1:5000/download/${encodeURIComponent(file.filename)}`
                    }));
                } else {
                    console.error('Failed to fetch uploaded scores');
                }
            } catch (error) {
                console.error('Error fetching uploaded scores', error);
            }
        }
    }
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
