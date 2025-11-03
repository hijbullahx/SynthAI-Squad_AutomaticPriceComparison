

VENV_DIR="$PWD/.venv"

if [ ! -d "$VENV_DIR" ]; then
  echo "Virtualenv not found at $VENV_DIR"
  echo "Create one with: python -m venv .venv"
  return 2 2>/dev/null || exit 2
fi


if [ -f "$VENV_DIR/bin/activate" ]; then
  . "$VENV_DIR/bin/activate"
  return 0 2>/dev/null || exit 0
fi

export VIRTUAL_ENV="$VENV_DIR"
_OLD_VIRTUAL_PATH="$PATH"
PATH="$VIRTUAL_ENV/Scripts:$PATH"
export PATH


if [ -n "${PYTHONHOME:-}" ]; then
  _OLD_VIRTUAL_PYTHONHOME="${PYTHONHOME:-}"
  unset PYTHONHOME
fi

if [ -z "${VIRTUAL_ENV_DISABLE_PROMPT:-}" ]; then
  _OLD_VIRTUAL_PS1="${PS1:-}"
  PS1="(.venv) ${PS1:-}"
  export PS1
fi

hash -r 2>/dev/null || true

deactivate_venv() {
  if [ -n "${_OLD_VIRTUAL_PATH:-}" ]; then
    PATH="${_OLD_VIRTUAL_PATH:-}"
    export PATH
    unset _OLD_VIRTUAL_PATH
  fi
  if [ -n "${_OLD_VIRTUAL_PYTHONHOME:-}" ]; then
    PYTHONHOME="${_OLD_VIRTUAL_PYTHONHOME:-}"
    export PYTHONHOME
    unset _OLD_VIRTUAL_PYTHONHOME
  fi
  if [ -n "${_OLD_VIRTUAL_PS1:-}" ]; then
    PS1="${_OLD_VIRTUAL_PS1:-}"
    export PS1
    unset _OLD_VIRTUAL_PS1
  fi
  unset VIRTUAL_ENV
  unset -f deactivate_venv
}

return 0 2>/dev/null || exit 0
