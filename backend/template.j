<div class="has-text-centered">
<div class="columns sentiment-column">
    <div class="column">
        <span class="icon has-text-dark tooltip is-tooltip-bottom" data-tooltip="Anger: {{ template_sentiments.get('Anger', 0.0) }}">
            <i class="fas fa-3x fa-angry"></i>
        </span>
    </div>
    <div class="column">
        <span class="icon has-text-dark tooltip is-tooltip-bottom" data-tooltip="Fear: {{ template_sentiments.get('Fear', 0.0) }}">
            <i class="fas fa-3x fa-ghost"></i>
        </span>
    </div>
    <div class="column">
        <span class="icon has-text-dark tooltip is-tooltip-bottom" data-tooltip="Joy: {{ template_sentiments.get('Joy', 0.0) }}">
            <i class="fas fa-3x fa-smile"></i>
        </span>
    </div>
    <div class="column">
        <span class="icon has-text-dark tooltip is-tooltip-bottom" data-tooltip="Sadness: {{ template_sentiments.get('Sadness', 0.0) }}">
            <i class="fas fa-3x fa-sad-tear"></i>
        </span>
    </div>
</div>

<div class="columns sentiment-column">
    <div class="column is-one-quarter is-offset-1">
        <span class="icon has-text-dark tooltip is-tooltip-bottom" data-tooltip="Analytical: {{ template_sentiments.get('Analytical', 0.0) }}">
            <i class="fas fa-3x fa-diagnoses"></i>
        </span>
    </div>
    <div class="column is-one-quarter">
        <span class="icon has-text-dark tooltip is-tooltip-bottom" data-tooltip="Confident: {{ template_sentiments.get('Confident', 0.0) }}">
            <i class="fas fa-3x fa-clipboard-check"></i>
        </span>
    </div>
    <div class="column is-one-quarter">
        <span class="icon has-text-dark tooltip is-tooltip-bottom" data-tooltip="Tentative: {{ template_sentiments.get('Tentative', 0.0) }}">
            <i class="fas fa-3x fa-history"></i>
        </span>
    </div>
</div>
</div>

<hr/>
{% for item in template_articles %}
<article class="media">
  <figure class="media-left">
    <p class="image is-64x64">
      <img src="{{ item['urlToImage']}}">
    </p>
  </figure>
  <div class="media-content">
    <div class="content">
      <a href="{{item['url']}}">
        {{item['title']}}
      </a>
    </div>
  </div>
</article>
{% endfor %}
