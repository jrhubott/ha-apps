# The Music Assistant server image built from the fork's source (the "server" context is the
# server's own Dockerfile), with the fork's frontend wheel in place of the pinned one.
# A source build has no bundled service credentials: the user's own come from
# MASS_APP_VARS_FILE, on the Home Assistant share mapped read-only into the app.
FROM server

COPY music_assistant_frontend-*.whl install_frontend.py /tmp/frontend/
RUN python /tmp/frontend/install_frontend.py /tmp/frontend \
    && rm -rf /tmp/frontend \
    && rm -f /app/build_info.json

ENV MASS_APP_VARS_FILE=/share/music_assistant_dev/app_vars.json

ARG APP_VERSION
ARG MASS_VERSION
ARG CHANNEL
ARG SERVER_REF
ARG FRONTEND_REF
ARG SOURCE_URL
LABEL \
    org.opencontainers.image.title="Music Assistant Server Edge (jrhubott)" \
    org.opencontainers.image.description="Music Assistant server ${MASS_VERSION} with fixes and features in progress. Unofficial build without the bundled service credentials." \
    org.opencontainers.image.source="${SOURCE_URL}" \
    org.opencontainers.image.version="${APP_VERSION}" \
    org.opencontainers.image.authors="jrhubott" \
    io.hass.version="${APP_VERSION}" \
    io.hass.name="Music Assistant Edge (jrhubott)" \
    io.hass.description="Music Assistant dev plus jrhubott's merged feature branches" \
    io.github.ha-apps.channel="${CHANNEL}" \
    io.github.ha-apps.server-ref="${SERVER_REF}" \
    io.github.ha-apps.frontend-ref="${FRONTEND_REF}"
