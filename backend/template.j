<div class="has-text-centered">
<div class="columns sentiment-column">
    <div class="column">
        <span class="icon {% if template_sentiments.get('Anger', 0) == 0 %} has-text-light {% else %} has-text-danger {% endif %} tooltip is-tooltip-bottom" data-tooltip="Anger: {{ template_sentiments.get('Anger', 0.0) *100 }} %">
            <i class="fas fa-3x fa-angry"></i>
        </span>
    </div>
    <div class="column">
        <span class="icon {% if template_sentiments.get('Fear', 0) == 0 %} has-text-light {% else %} has-text-info {% endif %} tooltip is-tooltip-bottom" data-tooltip="Fear: {{ template_sentiments.get('Fear', 0.0) *100 }} %">
            <i class="fas fa-3x fa-ghost"></i>
        </span>
    </div>
    <div class="column">
        <span class="icon {% if template_sentiments.get('Joy', 0) == 0 %} has-text-light {% else %} has-text-warning {% endif %} tooltip is-tooltip-bottom" data-tooltip="Joy: {{ template_sentiments.get('Joy', 0.0) *100 }} %">
            <i class="fas fa-3x fa-smile"></i>
        </span>
    </div>
    <div class="column">
        <span class="icon {% if template_sentiments.get('Sadness', 0) == 0 %} has-text-light {% else %} has-text-success {% endif %} tooltip is-tooltip-bottom" data-tooltip="Sadness: {{ template_sentiments.get('Sadness', 0.0) *100 }} %">
            <i class="fas fa-3x fa-sad-tear"></i>
        </span>
    </div>
</div>

<div class="columns sentiment-column">
    <div class="column is-one-quarter is-offset-1">
        <span class="icon {% if template_sentiments.get('Analytical', 0) == 0 %} has-text-light {% else %} has-text-primary {% endif %} tooltip is-tooltip-bottom" data-tooltip="Analytical: {{ template_sentiments.get('Analytical', 0.0) *100 }} %">
            <i class="fas fa-3x fa-diagnoses"></i>
        </span>
    </div>
    <div class="column is-one-quarter">
        <span class="icon {% if template_sentiments.get('Confident', 0) == 0 %} has-text-light {% else %} has-text-link {% endif %} tooltip is-tooltip-bottom" data-tooltip="Confident: {{ template_sentiments.get('Confident', 0.0) * 100 }} %">
            <i class="fas fa-3x fa-clipboard-check"></i>
        </span>
    </div>
    <div class="column is-one-quarter">
        <span class="icon {% if template_sentiments.get('Tentative', 0) == 0 %} has-text-light {% else %} has-text-dark {% endif %} tooltip is-tooltip-bottom" data-tooltip="Tentative: {{ template_sentiments.get('Tentative', 0.0) * 100 }} %">
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
      <a href="{{item['url']}}" target="_blank">
        {{item['title']}}
      </a>
    </div>
    {% for tone in item['tones'] %}
      {% if tone["tone_id"] == "anger" %}
        <span class="icon has-text-warning tooltip is-tooltip-top" data-tooltip="Anger: {{ tone["score"] *100 }} %">
            <i class="fas fa-angry"></i>
        </span>
      {% endif %}
      {% if tone["tone_id"] == "fear" %}
        <span class="icon has-text-warning tooltip is-tooltip-top" data-tooltip="Fear: {{ tone["score"] *100 }} %">
            <i class="fas fa-ghost"></i>
        </span>
      {% endif %}
      {% if tone["tone_id"] == "joy" %}
        <span class="icon has-text-warning tooltip is-tooltip-top" data-tooltip="Joy: {{ tone["score"] *100 }} %">
            <i class="fas fa-smile"></i>
        </span>
      {% endif %}
      {% if tone["tone_id"] == "sadness" %}
        <span class="icon has-text-warning tooltip is-tooltip-top" data-tooltip="Sadness: {{ tone["score"] *100 }} %">
            <i class="fas fa-sad-tear"></i>
        </span>
      {% endif %}
      {% if tone["tone_id"] == "analytical" %}
        <span class="icon has-text-warning tooltip is-tooltip-top" data-tooltip="Analytical: {{ tone["score"] *100 }} %">
            <i class="fas fa-diagnoses"></i>
        </span>
      {% endif %}
      {% if tone["tone_id"] == "confident" %}
        <span class="icon has-text-warning tooltip is-tooltip-top" data-tooltip="Confident: {{ tone["score"] *100 }} %">
            <i class="fas fa-clipboard-check"></i>
        </span>
      {% endif %}
      {% if tone["tone_id"] == "tentative" %}
        <span class="icon has-text-warning tooltip is-tooltip-top" data-tooltip="Tentative: {{ tone["score"] *100 }} %">
            <i class="fas fa-history"></i>
        </span>
      {% endif %}
    {% endfor %}
  </div>
</article>
{% endfor %}
