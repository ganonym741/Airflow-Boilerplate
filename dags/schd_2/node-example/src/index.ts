import fs from 'fs-extra';

async function readFileContent(filePath: string): Promise<void> {
  try {
    const content = await fs.readFile(filePath, 'utf-8');
    console.log(content);
  } catch (error) {
    throw Error(`Error reading file: ${error}`);
  }
}

const filePath = './sample.txt';
readFileContent(filePath);