 if (env | grep -Fq 'DISTROBOX'); then
	 command_not_found_handle() {
	 # don't run if not in a container
	   if [ ! -e /run/.containerenv ] && [ ! -e /.dockerenv ]; then
	     exit 127
	   fi
	   distrobox-host-exec "${@}"
	 }
	 if [ -n "${ZSH_VERSION-}" ]; then
	   command_not_found_handler() {
	     command_not_found_handle "$@"
	  }
	 fi
 fi


# If you come from bash you might have to change your $PATH.
export PATH=$HOME/bin:$HOME/.local/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"

# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
ZSH_THEME="agnoster"
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS="true"

# Uncomment the following line to disable colors in ls.
DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Add wisely, as too many plugins slow down shell startup.
plugins=(git z zsh-autosuggestions zsh-syntax-highlighting fzf-tab)

source $ZSH/oh-my-zsh.sh


# Added manually
# ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE="fg=#ff00ff,bg=cyan,bold,underline"

if ! (env | grep -Fq 'DISTROBOX'); then
eval "$(oh-my-posh init zsh --config ~/Developer/oh_my_posh_themes/3_shell.omp.json)"
fi
alias gdrive="google-drive-ocamlfuse ~/googledrive"
alias nano="micro"
alias sudo="sudo"




function workon(){
        if [ -z "$1" ]
        then
              echo "Trying to activate venv ..."
# source venv/bin/activate  # commented out by conda initialize
        else
              echo "Trying to activate environment $1 ..."
# source $1/bin/activate  # commented out by conda initialize
        fi
}

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
# [[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/tirtha/miniconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/tirtha/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/home/tirtha/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/tirtha/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<


[ -f ~/.fzf.zsh ] && source ~/.fzf.zsh



# eza config
alias ls='eza --icons=always $@'                                                          # ls
alias l='eza -lbF --git --icons=always $@'                                                # list, size, type, git
alias ll='eza -lbGF --git --icons=always $@'                                             # long list
alias llm='eza -lbGd --git --sort=modified --icons=always $@'                            # long list, modified date sort
alias la='eza -lbhHigUmuSa --time-style=long-iso --git --color-scale --icons=always $@'  # all list
alias lx='eza -lbhHigUmuSa@ --time-style=long-iso --git --color-scale --icons=always $@' # all + extended list


# disable sort when completing `git checkout`
zstyle ':completion:*:git-checkout:*' sort false
# set descriptions format to enable group support
# NOTE: don't use escape sequences here, fzf-tab will ignore them
zstyle ':completion:*:descriptions' format '[%d]'
# set list-colors to enable filename colorizing
zstyle ':completion:*' list-colors ${(s.:.)LS_COLORS}
# force zsh not to show completion menu, which allows fzf-tab to capture the unambiguous prefix
zstyle ':completion:*' menu no
# preview directory's content with eza when completing cd
zstyle ':fzf-tab:complete:cd:*' fzf-preview 'eza -1 --color=always $realpath'
# switch group using `<` and `>`
zstyle ':fzf-tab:*' switch-group '<' '>'


