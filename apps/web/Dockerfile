FROM node:22-alpine
WORKDIR /workspace
RUN corepack enable
COPY package.json pnpm-lock.yaml pnpm-workspace.yaml ./
COPY apps/web/package.json ./apps/web/package.json
RUN pnpm install --frozen-lockfile
COPY apps/web ./apps/web
EXPOSE 3000
CMD ["pnpm", "--filter", "@zar-horizon/web", "dev", "--hostname", "0.0.0.0"]
