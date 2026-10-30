import {mkdir,copyFile} from 'node:fs/promises';
await mkdir('dist',{recursive:true});
for(const f of ['index.html','styles.css','app.js','engine.js','brand-tokens.js','visualization.js','review-deck.js','submission-guide.js'])await copyFile(f,'dist/'+f);
console.log('Production assets built in dist/');
