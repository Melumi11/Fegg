# uses a light python 3
FROM python:3-alpine
# where files will go
WORKDIR /app
# pip install requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# I had to install yt-dlp like this cuz normal install throws error
# RUN python3 -m pip install --no-deps -U yt-dlp
# copy rest of my files - line below copies everything - need to use var for spaces
# COPY . .
COPY main.py client.py slashcommands.py token.txt .

# Make the entrypoint script executable
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

CMD ["/app/entrypoint.sh"]

# use commands below - I build for rpi - docker needs to be on
# docker buildx build -t fegg --platform linux/arm64 .
# docker image ls
# docker save {ID} -o ./image.tar

# to check build
# docker buildx build -o - . > image1.tar --platform linux/arm64